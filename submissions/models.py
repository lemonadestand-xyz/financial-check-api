import uuid

from django.db import models
from django.conf import settings

from django_extensions.db.models import TimeStampedModel


class Submission(TimeStampedModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )
    item = models.ForeignKey(
        'plaidapp.PlaidItem',
        null=True,
        default=None,
        on_delete=models.PROTECT
    )

    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    address = models.CharField(max_length=300)
    ssn = models.CharField(max_length=20)
    date_of_birth = models.DateField(blank=True, null=True, default=None)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    monthly_income = models.DecimalField(max_digits=7, decimal_places=2, null=True, default=None)
    credit_check_opt_in = models.BooleanField(default=False)
    status = models.CharField(default='pending', max_length=20)