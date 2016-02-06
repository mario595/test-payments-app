'''
Created on 6 Feb 2016

@author: mariopersonal
'''
from accounts.commands.notify_command import NotifyCommand
from accounts.commands.transfer_command import TransferCommand


class CommandFactory(object):
    
    def __init__(self):
        self._commands = {'TRANS': TransferCommand,
                          'NOTIFY': NotifyCommand}

    def create_command(self, typ, obj):
        target = typ.upper()
        return self._commands[target](obj)