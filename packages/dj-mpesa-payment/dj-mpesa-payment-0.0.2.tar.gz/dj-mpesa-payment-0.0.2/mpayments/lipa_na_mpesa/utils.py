import base64
import string

import phonenumbers
import requests
from django.conf import settings
from phonenumbers import PhoneNumberFormat


def short_code():
    return getattr(settings, 'MPESA_CONSUMER_KEY', None)


def mpesa_base_url():
    return getattr(settings, 'MPESA_BASE_URL', None)


def account_reference():
    return getattr(settings, 'ACCOUNT_REFERENCE', short_code())


def transaction_description():
    return getattr(settings, 'TRANSACTION_DESCRIPTION', short_code())


def confirmation_callback_url() -> str:
    return getattr(settings, 'CONFIRMATION_CALL_BACK_URL', 'http://localhost:8000/callback')


def validation_callback_url() -> str:
    return getattr(settings, 'VALIDATION_CALL_BACK_URL', 'http://localhost:8000/callback')


def pass_key() -> str:
    return getattr(settings, 'PASS_KEY', None)


def basic_authorization(consumer_key, consumer_secret):
    string_to_encode = "%s:%s" % (consumer_key, consumer_secret)
    encoded_string = base64.b64encode(string_to_encode.encode('utf-8'))
    return encoded_string.decode('utf-8')


def get_password(short_code, pass_key, timestamp):
    string_to_encode = "%s%s%s" % (short_code, pass_key, timestamp)
    encoded_string = base64.b64encode(string_to_encode.encode('utf-8'))
    return encoded_string.decode('utf-8')


def auth_response(authorization, base_url, requests):
    headers = {'Authorization': "Basic %s" % authorization}
    url = "%s/oauth/v1/generate?grant_type=client_credentials" % base_url
    return requests.request("GET", url=url, headers=headers)


def get_timestamp():
    from datetime import datetime
    now = datetime.now()
    return now.strftime("%Y%m%d%H%M%S")


def format_phone_number(phone_number) -> string:
    parsed_phone_number = phonenumbers.parse(phone_number, region='KE')
    formatted_phone_number = phonenumbers.format_number(parsed_phone_number, PhoneNumberFormat.E164)[1:]
    return formatted_phone_number


def get_access_token() -> string:
    consumer_key = getattr(settings, 'MPESA_CONSUMER_KEY', None)
    consumer_secret = getattr(settings, 'MPESA_CONSUMER_SECRET', None)
    if consumer_key is None:
        raise ValueError('MPESA_CONSUMER_KEY is not defined in Django settings.')

    if consumer_secret is None:
        raise ValueError('MPESA_CONSUMER_SECRET is not defined in Django settings.')

    if mpesa_base_url() is None:
        raise ValueError('MPESA_BASE_URL is not defined in Django settings.')

    try:
        authorization = basic_authorization(consumer_key, consumer_secret)
        response = auth_response(authorization, mpesa_base_url, requests)
        if response.status_code == 200:
            json_data = response.json()
            return json_data['access_token']
        return "Invalid Key"
    except KeyError:
        return "Invalid Key"

