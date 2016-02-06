'''
Created on 6 Feb 2016

@author: mariopersonal
'''
from accounts.transfer_command import TransferCommand
from accounts.notify_command import NotifyCommand


class CommandFactory(object):
    
    def __init__(self):
        self._commands = {'TRANS': TransferCommand,
                          'NOTIFY': NotifyCommand}

    def create_command(self, typ, obj):
        target = typ.upper()
        return self._commands[target](obj)