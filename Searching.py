"""
Author: Erutaner
Date: 2023.01.06
"""
import random

class SearchingTable:
    def __init__(self,my_ls):
        self.data = my_ls
        self.length = len(my_ls)

    def SequenceSearch(self,key):
        ipos = -1
        for i in range(self.length):
            if self.data[i] == key:
                ipos = i
                break
        return ipos
    def SequenceSearch1(self,key):
        self.data[0] = key
        ipos = -1
        for i in range(self.length-1,0,-1):
            if self.data[i] == key:
                ipos = i
                break
        return ipos

    def BinarySearch(self,key):
        low = 0
        high = self.length-1
        while low <= high:
            mid = int((low+high)/2)
            if key<self.data[mid]:
                high = mid-1
            elif key > self.data[mid]:
                low = mid + 1
            else:
                return mid
        return -1

def main():
    my_ls = []
    for i in range(15):
        rand = random.randint(0,20)
        my_ls.append(rand)
    my_ls = list(set(my_ls))
    print(f"The list is: {my_ls}")

    table_test = SearchingTable(my_ls)
    key = random.randint(0,20)
    print("The key to search is:",key)
    search = table_test.BinarySearch(key)
    if search == -1:
        print("Item not found.")
    else:
        print(f"Item found at position {search}")
main()