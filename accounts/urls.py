'''
Created on 5 Feb 2016

@author: mariopersonal
'''
from django.conf.urls import url

from accounts.views import transactions, payment


urlpatterns = [url(r'^transactions/', transactions, name='transactions'),
               url(r'^payment/', payment, name='payments'),
            ]

