import uuid

from django.db import models


class MpesaTransaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone_number = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    receipt_number = models.CharField(max_length=30, null=True, blank=True)
    merchant_request_id = models.CharField(max_length=30)
    checkout_request_id = models.CharField(max_length=100)
    result_code = models.CharField(max_length=20, null=True, blank=True)
    result_description = models.TextField(null=True, blank=True)
    is_finished = models.BooleanField(default=False)
    is_successful = models.BooleanField(default=False)
    is_utilised = models.BooleanField(default=False)
    transaction_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

