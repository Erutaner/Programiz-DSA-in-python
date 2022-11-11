"""
Author: Erutaner
Date: 2022.11.10
"""
import random
# Priority Queue implementation in Python
# it's worth noting that this is essentially a max(or min) heap.
class PriorityQueue():
    def __init__(self):
        self.array = []

    def heapify(self,cur):
        largest = cur
        left = 2 * cur + 1
        right = 2 * cur + 2
        if left < len(self.array) and self.array[left] > self.array[largest]:
            largest = left
        if right < len(self.array) and self.array[right] > self.array[largest]:
            largest = right
        if largest != cur:
            self.array[largest], self.array[cur] = self.array[cur], self.array[largest]
            self.heapify(largest) # only need to reheapify the changed subtree(with index "largest" as it's root).

    def enqueue(self,item):
        if len(self.array) == 0:
            self.array.append(item)
        else:
            self.array.append(item)
            for i in range(len(self.array)//2-1,-1,-1):
                self.heapify(i)

    def deletenode(self,item):
        if len(self.array) == 0:
            print("This queue is empty now.")
        else:
            i = 0
            while self.array[i] != item:
                i += 1
                continue
            self.array[i], self.array[len(self.array)-1] = self.array[len(self.array)-1],\
                                                           self.array[i]
            ret = self.array.pop()
            for i in range(len(self.array)//2-1,-1,-1):
                self.heapify(i)
            return ret
    def dequeue(self):  #as a priority queue, when you do the dequeue operation, the item with highest priority should be returned
        if len(self.array) == 0:
            print("This queue is empty now.")
        else:
            self.array[0], self.array[len(self.array) - 1] = self.array[len(self.array) - 1], \
                                                             self.array[0]
            ret = self.array.pop()
            for i in range(len(self.array)//2-1,-1,-1):
                self.heapify(i)
            return ret

def main():
    p_q = PriorityQueue()
    for i in range(10):
        tmp = random.randint(0, 10)
        p_q.enqueue(tmp)
        print("Insert item:", tmp, " now the priority queue is:", str(p_q.array))
        print()
    for i in range(10):
        deleted_item = p_q.dequeue()
        print("Remove the highest priority item:", deleted_item, " now the priority queue is:", str(p_q.array))
        print()
main()
