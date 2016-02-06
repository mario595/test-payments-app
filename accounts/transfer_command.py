'''
Created on 6 Feb 2016

@author: mariopersonal
'''
from accounts.commands import Command, CommandError


class TransferCommand(Command):
    
    def execute(self):
        if not self._are_accounts_different():
            raise SameAccountError('You have selected to make a transfer to the same account, please,\
            select different accounts and try again')
        if not self._is_balance_sufficient():
            transfer = self._obj
            raise FromAccountInsufficientBalanceError('The transfer of %0.2f was unsucessful as account %s \
                                                        has insufficient funds (%0.2f)' %
                                                      (transfer.amount, transfer.from_account.name, transfer.from_account.balance))
        self._make_transfer()
    
    def _are_accounts_different(self):
        return self._obj.from_account.id != self._obj.to_account.id
    
    def _is_balance_sufficient(self):
        return self._obj.from_account.balance >= self._obj.amount
    
    def _make_transfer(self):
        transfer = self._obj
        from_account = transfer.from_account
        to_account = transfer.to_account
        amount = transfer.amount
        
        from_account.balance = from_account.balance - amount
        to_account.balance = to_account.balance + amount
        
        from_account.save()
        to_account.save()
        transfer.save()

class SameAccountError(CommandError):
    pass
class FromAccountInsufficientBalanceError(CommandError):
    pass