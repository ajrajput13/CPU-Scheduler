'''
Author: Ansh Rajput
KUID: 3057528
Date: Monday, Feburary 21
Lab: lab 3
Last modified: Sunday, Feburary 27 
Purpose: The purpose of the Stack class is create a stack in which items
         can be added, removed, and checked to see if it is empty.
        
'''

from calls_class import Calls

class Stack:
    def __init__(self):
        self._top = None
    
    def push(self, entry): #Adds items to the stack
        new_top = Calls(entry)
        if self._top == None:
            self._top = new_top
        else:
            self._top.next = new_top
            self._top = new_top

    def pop(self): #Removes items from the stack
        if self._top != None:
            self._top = self._top.next
        else:
            raise RuntimeError('Stack empty')

    def peek(self): #Checks the top items in the stack
        if self._top != None:
            return self._top
        else:
            raise RuntimeError('Stack empty')

    def is_empty(self): #Checks if the stack is empty
        return self._top == None
    
