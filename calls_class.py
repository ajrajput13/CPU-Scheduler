'''
Author: Ansh Rajput
KUID: 3057528
Date: Monday, Feburary 21
Lab: lab 3
Last modified: Sunday, Feburary 27 
Purpose: The purpose of the Call class is to hold the code needed when another class
         calls it. When used with other classes and code, the call class will put
         that function the call stack.
        
'''

class Calls:
    def __init__(self, entry):
        self.entry = entry
        self.next = None
