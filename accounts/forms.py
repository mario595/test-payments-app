'''
Created on 5 Feb 2016

@author: mariopersonal
'''
from django import forms
from django.forms.models import ModelForm

from accounts.models import Transaction, Account


class AccountModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, account):
        return "%s - %2.0f" % (account.name, account.balance)

class TransactionForm(ModelForm):
    from_account = AccountModelChoiceField(queryset=Account.objects.filter(balance__gt=0))
    to_account = AccountModelChoiceField(queryset=Account.objects.all())
    class Meta:
        model = Transaction
        fields = ['from_account', 'to_account', 'amount']
        
