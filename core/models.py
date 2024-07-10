from django.db import models


class Txn(models.Model):
    block_number = models.IntegerField()
    timestamp = models.IntegerField()
    transaction_hash = models.CharField(max_length=66, unique=True)
    nonce = models.IntegerField()
    block_hash = models.CharField(max_length=66)
    transaction_index = models.IntegerField()
    from_address = models.CharField(max_length=42)
    to_address = models.CharField(max_length=42)
    value = models.CharField(max_length=255)
    gas = models.CharField(max_length=255)
    gas_price = models.CharField(max_length=255)
    is_error = models.CharField(max_length=255)
    txreceipt_status = models.CharField(max_length=255)
    input = models.CharField(max_length=255)
    contract_address = models.CharField(max_length=255)
    cumulative_gas_used = models.CharField(max_length=255)
    gas_used = models.CharField(max_length=255)
    confirmations = models.CharField(max_length=255)
    method_id = models.CharField(max_length=255)
    function_name = models.CharField(max_length=255)

    class Meta:
        ordering = ['timestamp']