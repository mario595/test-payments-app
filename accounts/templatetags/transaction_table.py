'''
Created on 6 Feb 2016

@author: mariopersonal
'''
from django import template


register = template.Library()


@register.inclusion_tag('accounts/transaction_table.html')
def transaction_table(transfers):
    return {'transfers':transfers}
