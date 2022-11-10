"""
Author: Erutaner
Date: 2022.11.10
"""
import random

# This is a simple Max Heap
class Max_Heap():
    def __init__(self):
        self.array = []
    def heapify(self,i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(self.array) and self.array[largest] < self.array[left]:
            largest = left
        if right < len(self.array) and self.array[largest] < self.array[right]:
            largest = right
        if largest != i:
            self.array[i],self.array[largest] = self.array[largest], self.array[i]
            self.heapify(largest)
    def insert(self,item):
        if len(self.array) == 0:
            self.array.append(item)
        else:
            self.array.append(item)
            for i in range((len(self.array)//2)-1,-1,-1):
                self.heapify(i)
    def deleteNode(self,num):
        i = 0
        for i in range(0,len(self.array)):
            if self.array[i] == num:
                break
        self.array[i], self.array[len(self.array)-1] = self.array[len(self.array)-1],\
                                                       self.array[i]
        ret = self.array.pop()
        for i in range((len(self.array)//2)-1,-1,-1):
            self.heapify(i)
        return ret

def main():
    max_heap = Max_Heap()
    for i in range(10):
            tmp = random.randint(0, 10)
            max_heap.insert(tmp)
            print("Insert item:",tmp,"now the tree array is:",str(max_heap.array))
            print()
    for i in range(10):
        rand_index = random.randint(0, len(max_heap.array) - 1)
        deleted_item = max_heap.deleteNode(max_heap.array[rand_index])
        print("Delete node:",deleted_item,"now the tree array is:",str(max_heap.array))
        print()
main()

