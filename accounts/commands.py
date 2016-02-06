'''
Created on 6 Feb 2016

@author: mariopersonal
'''
class Command(object):
    def __init__(self, obj):
        self._obj = obj
    def execute(self):
        raise NotImplementedError
    
class CommandError(Exception):
    pass