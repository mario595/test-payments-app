'''
Created on 6 Feb 2016

@author: mariopersonal
'''
import django.test

from accounts.models import Account, Transaction
from accounts.commands.transfer_command import TransferCommand, SameAccountError, \
    FromAccountInsufficientBalanceError


class TestTransferCommands(django.test.TestCase):
    
    def setUp(self):
        self.ac1 = Account.objects.create(name='ac1', email='ac1@mail.com', balance=200)
        self.ac2 = Account.objects.create(name='ac2', email='ac2@mail.com', balance=0)
        self.ac3 = Account.objects.create(name='ac3', email='ac3@mail.com', balance=500)
        self.ac4 = Account.objects.create(name='ac4', email='ac4@mail.com', balance=10)
    
    def testTransferCommandExecuteWithSameAccount(self):
        try:
            transfer = Transaction(from_account=self.ac1, to_account=self.ac1, amount=1)
            cmd = TransferCommand(transfer)
            cmd.execute()
            self.assertTrue(False, 'Exception should be raised')
        except SameAccountError:
            pass
    
    def testTransferCommandExecuteWithDifferentAccountsAndZeroBalance(self):
        try:
            transfer = Transaction(from_account=self.ac2, to_account=self.ac1, amount=1)
            cmd = TransferCommand(transfer)
            cmd.execute()
            self.assertTrue(False, 'Exception should be raised')
        except FromAccountInsufficientBalanceError:
            pass
    
    def testTransferCommandExecuteWithInsufficientBalance(self):
        try:
            transfer = Transaction(from_account=self.ac4, to_account=self.ac3, amount=11)
            cmd = TransferCommand(transfer)
            cmd.execute()
            self.assertTrue(False, 'Exception should be raised')
        except FromAccountInsufficientBalanceError:
            pass
    
    def testTransferCommandExecuteWithExactBalance(self):
        try:
            transfer = Transaction(from_account=self.ac4, to_account=self.ac3, amount=10)
            cmd = TransferCommand(transfer)
            cmd.execute()
            self.assertEquals(self.ac4.balance, 0)
            self.assertEquals(self.ac3.balance, 510)
            
        except Exception as e:
            self.assertTrue(False, "Exception shouldn't be raised: %s" % e)
    
    def testTransferCommandExecuteSuccessToZeroBalanceAccount(self):
        try:
            transfer = Transaction(from_account=self.ac1, to_account=self.ac2, amount=10)
            cmd = TransferCommand(transfer)
            cmd.execute()
            self.assertEquals(self.ac1.balance, 190)
            self.assertEquals(self.ac2.balance, 10)
            
        except Exception as e:
            self.assertTrue(False, ("Exception shouldn't be raised: %s" % e))
    
    def testTransferCommandExecuteSuccess(self):
        try:
            transfer = Transaction(from_account=self.ac1, to_account=self.ac3, amount=10)
            cmd = TransferCommand(transfer)
            cmd.execute()
            self.assertEquals(self.ac1.balance, 190)
            self.assertEquals(self.ac3.balance, 510)
             
        except Exception as e:
            self.assertTrue(False, "Exception shouldn't be raised: %s" % e)