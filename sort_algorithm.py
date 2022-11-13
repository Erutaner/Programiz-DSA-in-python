"""
Author: Erutaner
Date: 2022.11.13
"""
def op_bubble_sort(arr):
    for i in range(len(arr)-1):
        swapped = False
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
arr = [5,4,3,2,1,100]
op_bubble_sort(arr)
print(arr)
