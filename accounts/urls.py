'''
Created on 5 Feb 2016

@author: mariopersonal
'''
from django.conf.urls import patterns, url

from accounts.views import transactions, payment


urlpatterns = patterns('accounts.views',
                       url(r'^transactions/', transactions, name='transactions'),
                       url(r'^payment/', payment, name='payment'),
            )

