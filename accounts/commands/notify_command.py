'''
Created on 6 Feb 2016

@author: mariopersonal
'''
from django.core.mail import send_mass_mail

from accounts.commands.commands import Command

'''
This is a NotifyCommand. It is used to notify the users involved in a transaction. The notification
is being made through an email.
'''
class NotifyCommand(Command):
    
    def execute(self):
        transfer = self._obj
        origin_body = 'There has been a transfer of %0.2f from your account to the account %s' % (transfer.amount, transfer.to_account)
        recipient_body = 'You have received %0.2f from the account %s' % (transfer.amount, transfer.to_account)
        
        message_origin = ('Transfer from your account',
                          origin_body, 
                          'payments@mail.com', [self._obj.from_account.email])
        message_recipient = ('Transfer to your account',
                          recipient_body, 
                          'payments@mail.com', [self._obj.to_account.email])
        send_mass_mail((message_origin, message_recipient), fail_silently=False)
