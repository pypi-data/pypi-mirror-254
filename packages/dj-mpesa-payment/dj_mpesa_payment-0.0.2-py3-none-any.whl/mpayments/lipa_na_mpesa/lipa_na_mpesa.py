from .utils import *


class LipaNaMpesa:
    def __init__(self):
        self.shortcode = short_code()
        self.token = get_access_token()
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': "Bearer %s" % self.token
        }

    def stk_push(self, phone_number, amount, a):
        timestamp = get_timestamp()
        url = '%s/mpesa/stkpush/v1/processrequest' % mpesa_base_url()
        password = get_password(174379, pass_key(), timestamp)
        payload = {
            "BusinessShortCode": self.shortcode,
            "Password": password,
            "Timestamp": "%s" % timestamp,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone_number,
            "PartyB": self.shortcode,
            "PhoneNumber": phone_number,
            "CallBackURL": confirmation_callback_url(),
            "AccountReference": account_reference(),  # Company Account Number
            "TransactionDesc": transaction_description()
        }
        response = requests.request("POST", url=url, headers=self.headers, json=payload)
        return response

    def c2b_checkout(self):
        pass

    def register_callbacks(self):
        url = "%s/mpesa/c2b/v1/registerurl" % mpesa_base_url()
        headers = self.headers
        payload = {
            "ShortCode": self.shortcode,
            "ResponseType": "Completed",
            "ConfirmationURL": confirmation_callback_url(),
            "ValidationURL": validation_callback_url()
        }
        response = requests.request("POST", url=url, headers=headers, json=payload)
        return response
