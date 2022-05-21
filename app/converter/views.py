from django.shortcuts import render
from .models import Currency
from .manager import convert


# Create your views here.
def index(request):
    currencies = Currency.objects.values_list('currency_code', 'currency_code_l').all()
    if request.method == 'POST':
        print(request.POST)
        context = {
            'from_curr': int(request.POST['from']),
            'to_curr': int(request.POST['to']),
            'summ': request.POST['summ'],
            'currencies': currencies,
            'result': convert(request.POST['summ'], request.POST['from'], request.POST['to'])
        }
        return render(request, 'converter/index.html', context=context)
    context = {'currencies': currencies}

    return render(request, 'converter/index.html', context=context)
