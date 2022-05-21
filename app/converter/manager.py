from datetime import datetime, timezone
from .models import Currency
import requests


def update_currency():
    Currency.objects.update_or_create(currency_code=980,
                                      defaults={'currency_code': 980, 'currency_code_l': 'UAH', 'units': 1,
                                                'amount': 1.0, 'update_time': datetime.now(timezone.utc)})
    response = requests.get('https://bank.gov.ua/NBU_Exchange/exchange?json').json()
    if response:
        for currency in response:
            Currency.objects.update_or_create(currency_code=currency['CurrencyCode'],
                                              defaults={'currency_code': currency['CurrencyCode'],
                                                        'currency_code_l': currency['CurrencyCodeL'],
                                                        'units': currency['Units'],
                                                        'amount': currency['Amount'],
                                                        'update_time': datetime.now(timezone.utc)})


def convert(amount, pay, receive):
    if (datetime.now(timezone.utc) - Currency.objects.get(pk=int(pay)).update_time).seconds > 3600:
        update_currency()
    pay_object = Currency.objects.get(pk=int(pay))
    receive_object = Currency.objects.get(pk=int(receive))
    result = float(amount) * pay_object.amount / pay_object.units / receive_object.amount * receive_object.units
    return result
