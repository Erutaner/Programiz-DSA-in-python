"""
Author: Erutaner
Date: 2022.11.07
"""
class Stack:
    '''This is a copy of the textbook code'''
    def __init__(self):
        self.MaxStackSize = 10
        self.lst = [None for x in range(0,self.MaxStackSize)]
        self.top = -1
    def IsEmptyStack(self):
        if self.top == -1: return True
        else: return False
    def Push(self,item):
        if self.top < self.MaxStackSize - 1:
            self.top += 1
            self.lst[self.top] = item
        else:
            print("This stack is full now.")
    def Pop(self):
        if self.IsEmptyStack():
            print("This stack is already empty.")
        else:
            self.top -= 1
            return self.lst[self.top+1]
    def Peek(self):
        if self.IsEmptyStack():
            print("This stack is empty now.")
            return
        return self.lst[self.top]

def main():
    stack = Stack()
    for i in range(10):
        stack.Push(i)
    j = 0
    while j < 10:
        print("The {}th item in this stack (from bottom to top) is:".format(stack.top+1),\
              stack.Pop())
        if not stack.IsEmptyStack():
            print("The current top stack item is:",stack.Peek())
        j += 1
main()