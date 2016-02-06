from __future__ import unicode_literals

from decimal import Decimal

from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=50, unique=True)
    balance = models.DecimalField(max_digits=8, decimal_places=2, default=Decimal('200'))
    email = models.EmailField()
    
    def __unicode__(self):
        return "%s - %2.0f" % (self.name, self.balance);
    
class Transaction(models.Model):
    from_account = models.ForeignKey(Account, related_name='from_transaction', on_delete=models.CASCADE)
    to_account = models.ForeignKey(Account, related_name='to_transaction', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)

