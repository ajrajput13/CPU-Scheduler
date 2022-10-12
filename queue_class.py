'''
Author: Ansh Rajput
Date: Monday, Feburary 21
Last modified: Sunday, Feburary 27 
Purpose: The purpose of the Queue class is to add items to the back of the queue,
         remove items from the front of the queue, return items in the front of
         the queue, and check to see if the queue is empty or not.    
'''

class Queue:
    def __init__(self):
        self._front = None
        self._back = None

    def enqueue(self, entry): #Adds item to the back of the queue
        new_back = entry
        if self.is_empty():
            self._front = new_back
            self._back = new_back
        else:
            self._back.next = new_back
            self._back = new_back
            self._back.next = None

    def dequeue(self): #Removes item from the front of the queue. Returns that item
        front_value = self.peek_front()
        self._front = self._front.next
        return front_value

    def peek_front(self): #Returns item in the front of the queue
        if self.is_empty():
            raise RuntimeError('Stack empty')
        else:
            return self._front

    def is_empty(self): #Checks if the queue is empty
        return self._front == None
