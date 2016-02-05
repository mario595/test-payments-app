'''
Created on 5 Feb 2016

@author: mariopersonal
'''

from django.core.urlresolvers import reverse
from django.test import Client
import django.test

from accounts.models import Account


class TestViews(django.test.TestCase):

    def setUp(self):
        pass
    
    def testTransactionsWithoutAccounts(self):
        
        client = Client()
        response = client.get(reverse('transactions'))
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context['accounts'].count(), 0)
    
    def testTransactionsWithAccounts(self):
        Account.objects.create(name="a1", balance=100.10, email="a1@mail.com")
        Account.objects.create(name="a2", balance=200.99, email="a2@mail.com")
        Account.objects.create(name="a3", balance=4200.98, email="a3@mail.com")
        
        client = Client()
        response = client.get(reverse('transactions'))
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context['accounts'].count(), 3)
