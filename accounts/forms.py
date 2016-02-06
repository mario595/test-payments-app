'''
Created on 5 Feb 2016

@author: mariopersonal
'''
from django import forms
from django.forms.models import ModelForm

from accounts.models import Transaction, Account


class TransactionForm(ModelForm):
    from_account = forms.ModelChoiceField(queryset=Account.objects.filter(balance__gt=0))
    to_account = forms.ModelChoiceField(queryset=Account.objects.all())
    class Meta:
        model = Transaction
        fields = ['from_account', 'to_account', 'amount']