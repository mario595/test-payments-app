'''
Created on 6 Feb 2016

@author: mariopersonal
'''
import django.test

from accounts.commands.command_factory import CommandFactory
from accounts.models import Transaction, Account


class TestTransferCommands(django.test.TestCase):
    
    def setUp(self):
        self.command_factory = CommandFactory()
    
    def test_get_trans_command(self):
        transaction = Transaction(Account(), Account(), 100)
        cmd = self.command_factory.create_command("TRANS", transaction)
        self.assertEquals(cmd._obj, transaction)
        