import json

from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from . import serializers
from .helpers import (
    write_json_to_file,
    check_payment,
    confirm_payment_by_merchant_id,
    confirm_payment_by_transaction_code,
    confirm_payment_by_phone
)
from .lipa_na_mpesa.lipa_na_mpesa import LipaNaMpesa
from .lipa_na_mpesa.utils import format_phone_number
from .models import MpesaTransaction
from .serializers import PaymentSuccessSerializer, MpesaTransactionSerializer


class MpesaPaymentViewSet(viewsets.ViewSet):
    lipa_na_mpesa = LipaNaMpesa()

    @action(
        detail=False, methods=['POST'],
        url_path='initiate-mpesa-payment',
        permission_classes=[permissions.IsAuthenticated]
    )
    def initiate_stk_push(self, request):
        data = request.data
        serializer = serializers.CheckoutSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        amount = serializer.validated_data['amount']
        raw_number = serializer.validated_data['phone_number']
        formatted_phone = format_phone_number(raw_number)
        response = self.lipa_na_mpesa.stk_push(amount=amount, phone_number=formatted_phone)
        json_data = response.json()
        if response.status_code != status.HTTP_200_OK:
            return Response(data=json_data, status=response.status_code)
        if json_data['ResponseCode'] != str(0):
            return Response(data=json_data, status=response.status_code)
        merchant_id = json_data['MerchantRequestID']  # '29115-34620561-1'
        checkout_id = json_data['CheckoutRequestID']  # 'ws_CO_191220191020363925'
        payment = check_payment(merchant_id, checkout_id)
        if payment:
            data = {'message': 'Payment successful. You are ready to proceed'}
            return Response(data=data, status=status.HTTP_201_CREATED)
        data = {'message': 'Failed to confirm payment.'}
        return Response(data=data, status=status.HTTP_404_NOT_FOUND)

    @action(
        detail=False, methods=['POST'],
        url_path='check-payments',
        permission_classes=[permissions.IsAuthenticated]
    )
    def check_payments(self, request):
        payment = None
        data = request.data
        merchant_id = data.get('merchant_id', None)
        checkout_id = data.get('checkout_id', None)
        phone_number = data.get('phone_number', None)
        transaction_code = data.get('transaction_code', None)
        if merchant_id and checkout_id:
            payment = confirm_payment_by_merchant_id(merchant_id, checkout_id)
        if phone_number is not None:
            payment = confirm_payment_by_phone(format_phone_number(phone_number))
        if transaction_code is not None:
            payment = confirm_payment_by_transaction_code(transaction_code)
        if payment is None:
            return Response(data={"ResultCode": 1000}, status=status.HTTP_404_NOT_FOUND)
        payment.is_utilised = True
        payment.save()
        serializer = MpesaTransactionSerializer(instance=payment)
        serializer.is_valid(raise_exception=True)
        return Response(data={"ResultCode": 0, "payment": serializer.data}, status=status.HTTP_200_OK)

    @csrf_exempt
    @action(detail=False, methods=['POST'], url_path='transactions', permission_classes=[permissions.AllowAny])
    def insert_payment_transaction(self, request):
        write_json_to_file(json, request.data, 'request.json')
        data = json.loads(json.dumps(request.data))
        write_json_to_file(json, data, 'request_dump.json')

        serializer = PaymentSuccessSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        body = serializer.validated_data['Body']
        stk_callback = body["stkCallback"]
        merchant_request_id = stk_callback["MerchantRequestID"]
        checkout_request_id = stk_callback["CheckoutRequestID"]
        result_code = stk_callback["ResultCode"]
        result_desc = stk_callback["ResultDesc"]
        callback_metadata = stk_callback["CallbackMetadata"]
        item = callback_metadata["Item"]
        amount = item[0]["Value"]
        receipt_number = item[1]["Value"]
        transaction_date = item[2]["Value"]
        phone_number = item[3]["Value"]

        try:
            transaction = MpesaTransaction(
                merchant_request_id=merchant_request_id,
                checkout_request_id=checkout_request_id,
                phone_number=phone_number,
                amount=amount,
                receipt_number=receipt_number,
                result_code=result_code,
                result_description=result_desc,
                is_finished=True,
                is_successful=True
            )
            transaction.save()
            serializer = MpesaTransactionSerializer(instance=transaction)
            serializer.is_valid(raise_exception=True)
            return Response(
                data={"ResultCode": 0, "ResultDesc": "Payment Completed successfully", "payment": serializer.data}
            )
        except ValueError:
            return Response(data={"ResultCode": 1000, "ResultDesc": "Failed to save payment"})

    @action(
        detail=False,
        methods=['GET'],
        url_path='register-callbacks',
        permission_classes=[permissions.IsAuthenticated]
    )
    def register_callbacks(self, request):
        response = self.lipa_na_mpesa.register_callbacks()
        return Response(data=response.json(), status=response.status_code)
