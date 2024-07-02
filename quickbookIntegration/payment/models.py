from django.db import models
import uuid

# Define payment status choices
PAYMENT_STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('completed', 'Completed'),
    ('failed', 'Failed'),
]

class Transaction(models.Model):
    trans_id = models.CharField(max_length=255, primary_key=True, default=uuid.uuid4, editable=False)
    amount = models.FloatField()
    order_id = models.CharField(max_length=255, null=True, blank=True)
    payment_status = models.CharField(max_length=255, choices=PAYMENT_STATUS_CHOICES, default='completed')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.trans_id)
