import time

from payments.models import MpesaTransaction


def write_json_to_file(json, data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


def check_payment(merchant_id, checkout_id):
    payment_record = None
    start_time = time.time()
    while time.time() - start_time < 45:
        payment_record = MpesaTransaction.objects.filter(
            merchant_request_id=merchant_id,
            checkout_request_id=checkout_id
        ).first()
        if payment_record:
            break
        else:
            time.sleep(1)
    return payment_record


def confirm_payment_by_merchant_id(merchant_id, checkout_id):
    payment_record = MpesaTransaction.objects.filter(
        merchant_request_id=merchant_id,
        checkout_request_id=checkout_id
    ).first()
    return payment_record


def confirm_payment_by_phone(phone_number):
    payment_record = MpesaTransaction.objects.filter(
        phone_number=phone_number,
        is_finished=True,
        is_successful=True,
        is_utilised=False
    ).first()
    return payment_record


def confirm_payment_by_transaction_code(transaction_code):
    payment_record = MpesaTransaction.objects.filter(
        receipt_number=transaction_code,
        is_finished=True,
        is_successful=True,
        is_utilised=False
    ).first()
    return payment_record
