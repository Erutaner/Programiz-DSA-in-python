"""
Author: Erutaner
Date: 2022.11.10
"""
import random
# Circular Queue implementation in Python
class CircularQueue():
    "The complexity of the enqueue and dequeue operations is O(1)"
    def __init__(self,length):
        self.length = length
        self.queue = [None for i in range(length)]
        self.head = -1
        self.rear = -1
    # Insert an element
    def enqueue(self,item):
        if ((self.rear + 1) % self.length) == self.head:
            print("This queue is full now.")
        elif self.head == -1:
            self.head += 1
            self.rear += 1
            self.queue[self.rear] = item
        else:
            self.rear = (self.rear + 1) % self.length
            self.queue[self.rear] = item
    # Delete and return an element
    def dequeue(self):
        if (self.rear == -1):
            print("This queue is empty now.")
        elif self.rear == self.head:
            temp = self.queue[self.rear]
            self.rear = -1
            self.head = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.length
            return temp
        # Show the current queue
    def showqueue(self):
        if (self.head == -1):
            print("This queue is empty now.")
        elif self.head <= self.rear:
            for i in range(self.head,self.rear+1):
                print(self.queue[i],end = " ")
            print('')
        else:
            for i in range(self.head,self.length):
                print(self.queue[i],end = " ")
            for i in range(self.rear+1):
                print(self.queue[i],end = " ")
            print('')
    # If the current queue is full or empty, return False and then stop the test.
    def test_continue(self):
        return not((self.rear == -1) or (((self.rear + 1) % self.length) == self.head))
    def is_empty(self):
        if self.rear == -1:
            return True
        else:
            return False
def main():
    c_q = CircularQueue(10)
    c_q.enqueue(0)
    while c_q.test_continue():
        choice = random.randint(0,11)
        if (choice % 3 == 0) or (choice % 3 == 1):
            tmp = random.randint(0,10)
            print("Insert an item:",tmp)
            c_q.enqueue(tmp)
            c_q.showqueue()
        else:
            print('Remove an item:',c_q.dequeue())
            c_q.showqueue()
