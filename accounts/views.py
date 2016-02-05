from django.http.response import HttpResponse
from django.shortcuts import render


def transactions(request):
    return HttpResponse("Hello transactions")

def payment(request):
    return HttpResponse("Hello payment")
