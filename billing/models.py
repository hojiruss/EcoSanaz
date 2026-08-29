import datetime

from django.db import models

from accounts.models import Users
from core.models import Packages


class UserPayments(models.Model):
    class PaymentStatus(models.TextChoices):
        PROCESSING = 'PROCESSING'
        COMPLETED = 'COMPLETED'
        FAILED = 'FAILED'

    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    package_id = models.ForeignKey(Packages, on_delete=models.CASCADE)
    status = models.CharField(
        choices=PaymentStatus.choices,
    )
    created_at = models.DateField(default=datetime.date.today)
    deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'user_payments'
        verbose_name = 'user_payments'
        ordering = ['created_at']