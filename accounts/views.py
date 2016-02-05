from django.http.response import HttpResponse
from django.shortcuts import render

from accounts.models import Account


def transactions(request):
    accounts = Account.objects.all()
    context = {'accounts':accounts}
    return HttpResponse(render(request, 'accounts/transactions.html', context))

def payment(request):
    return HttpResponse(render(request, 'accounts/payment.html', {}))
