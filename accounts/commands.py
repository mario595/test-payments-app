'''
Created on 6 Feb 2016

@author: mariopersonal
'''
class Invoker(object):
    @classmethod
    def execute(cls, command):
        command.execute()
        
class Command(object):
    def __init__(self, obj):
        self._obj = obj
    def execute(self):
        raise NotImplementedError