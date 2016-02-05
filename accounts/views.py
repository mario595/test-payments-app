from django.http.response import HttpResponse
from django.shortcuts import render


def transactions(request):
    return HttpResponse(render(request, 'accounts/transactions.html', {}))

def payment(request):
    return HttpResponse(render(request, 'accounts/payment.html', {}))
