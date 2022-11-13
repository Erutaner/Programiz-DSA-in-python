"""
Author: Erutaner
Date: 2022.11.13
"""
def bubble_sort(arr):
    for i in range(len(arr)-1):    #设共n个元素，则共需要排n-1次
        for j in range(len(arr)-i-1):   #外层游标取i时，已经进行了0,...,i-1 = i轮，排好了i个
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            else:
                continue
arr = [5,4,3,2,1]
bubble_sort(arr)
print(arr)