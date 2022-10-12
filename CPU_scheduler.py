'''
Author: Ansh Rajput
KUID: 3057528
Date: Monday, Feburary 21
Lab: lab 3
Last modified: Sunday, Feburary 27 
Purpose: The purpose of driver is to use the other classes such as Node and Queue to create
         a mock CPU scheduler. It also holds the main which reads given file and then calls
         specific functions from different classes based on what the user wrote.
'''

from node_class import Node
from queue_class import Queue

def main():
    while True:
        try:
            read_file = open(str(input("File name: ")))
            queue = Queue()
            for line in read_file:
                words = line.split()
                index=0
                for word in words:
                    if word == "START":
                        node = Node(words[index+1])
                        queue.enqueue(node)
                        node.stack_calls.push("main")
                        print(f'{words[index+1]} added to queue')
                    elif word == "CALL":
                        queue.peek_front().stack_calls.push(words[index+1])
                        removed_queue = queue.dequeue()
                        print(f'{removed_queue.entry} calls {words[index+1]}')
                        queue.enqueue(removed_queue)
                    elif word == "RETURN":
                        stack_top = queue.peek_front().stack_calls.peek()
                        print(f'{queue.peek_front().entry} returns from {stack_top.entry}')
                        if (stack_top.entry != "main"):
                            stack_top.pop()
                            queue.enqueue(queue.dequeue())
                        else:
                            print(f'{queue.peek_front().entry} process has ended')
                            queue.dequeue()
                    index+=1
            break
        except FileNotFoundError:
            print("File not found")

main()
