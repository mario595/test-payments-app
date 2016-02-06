'''
Created on 6 Feb 2016

@author: mariopersonal
'''

'''
This represents an abstract class for Command. Each subclass should implement an execute method.
'''
class Command(object):
    def __init__(self, obj):
        self._obj = obj
    def execute(self):
        raise NotImplementedError

'''
This represents generic Command error exception, each Command subclass should provide its own custom Exception subclassing
this. 
'''
class CommandError(Exception):
    pass