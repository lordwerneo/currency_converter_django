from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from datetime import datetime, timezone


# Create your models here.
class Currency(models.Model):
    currency_code = models.IntegerField(primary_key=True, unique=True, )
    currency_code_l = models.TextField(max_length=3, unique=True, validators=[MinLengthValidator(3),
                                                                              MaxLengthValidator(3)])
    units = models.IntegerField(blank=False)
    amount = models.FloatField(blank=False)
    update_time = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return f'{self.units} of {self.currency_code_l} costs {self.amount} UAH'
