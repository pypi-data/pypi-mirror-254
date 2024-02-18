# Mpesa Payment Lib
An Mpesa payment library for django framework

# Getting Started Guide

## Project description
This is a simple payment library to help you implement Mpesa payment in your dango application.

It's give all the required utility functions and methods to seamlessly work with mpesa

## Installation
It's very simple to install. Use:

`pip install dj-mpesa-payment` or `pipenv install dj-mpesa-payment` when using pip and pipenv respectively

## Setup

In your project's top level `setting.py` file, define the following mandatory variable;
- MPESA_CONSUMER_KEY = `consumer_key`
  - This is a consumer key from daraja developers account
 

- MPESA_CONSUMER_SECRET = `secret_key`
  - This key is also obtained from daraja developers account


- MPESA_BASE_URL = `mpesa_api_base_url`
  - This is the Mpesa api end point. For example the sandbox base url is https://sandbox.safaricom.co.ke
  - Remember not to include trailing `/` in the `base url`


- CONFIRMATION_CALL_BACK_URL = `your_confirm_url_endpoint`
  - This is a POST endpoint in your project that Safaricom will be sending the payment confirmation data successful payments


- VALIDATION_CALL_BACK_URL = `your_validation_url_endpoint`.
  - Not yet implemented. Read more on daraja api documentation


- PASS_KEY = `pass_key`
  - This key is as well obtained from daraja developers account


- SHORT_CODE = `your_paybill_or_till_number`


- ACCOUNT_REFERENCE = `your_organisation_name`
  - This is your organisation's name


- TRANSACTION_DESCRIPTION = `transaction_description`
  - This is a short text describing to user when the stk push pops what this transaction is for

Also, add in your `setting.py`, add the app in the `INSTALLED_APP` as 
```
INSTALLED_APPS = [
  #Other apps
  'mpayments',
]
```

## Usage
### Coming Soon. 

For guidance, contact the [Author](mailto:zeffah.elly@gmail.com)
