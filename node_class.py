'''
Author: Ansh Rajput
Date: Monday, Feburary 21
Last modified: Sunday, Feburary 27 
Purpose: The purpose of the Node class is to hold the code needed when another class
         calls it. It uses the Stack class to implement code so that the Queue class works.
        
'''

from stack_class import Stack

class Node:
    def __init__(self, entry):
        self.entry = entry
        self.next = None
        self.stack_calls = Stack()
