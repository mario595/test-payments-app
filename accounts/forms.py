'''
Created on 5 Feb 2016

@author: mariopersonal
'''
from django import forms
from django.forms.models import ModelForm

from accounts.models import Transaction, Account


class TransactionForm(ModelForm):
    from_account = forms.ChoiceField(choices=[(account.id, "%s - %0.2f" % (account.name, account.balance)) for account in Account.objects.all()])
    to_account = forms.ChoiceField(choices=[(account.id, "%s - %0.2f" % (account.name, account.balance)) for account in Account.objects.all()])
    class Meta:
        model = Transaction
        fields = ['from_account', 'to_account', 'amount']