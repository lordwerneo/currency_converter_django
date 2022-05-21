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
