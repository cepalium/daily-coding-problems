# -------------------------------------
# Author: Tuan Nguyen
# Date: 20190710
#!solutions/58.py
# -------------------------------------
"""
An sorted array of integers was rotated an unknown number of times.

Given such an array, find the index of the element in the array in faster than linear time. 
If the element doesn't exist in the array, return null.

For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, 
return 4 (the index of 8 in the array).

You can assume all the integers in the array are unique.
"""


def binarySearch(arr, k, pivot):
    # input: array 'arr' of rotated sorted array, target int k, int pivot
    # output: index of k in arr
    # method: binary search
    # running time: O(logn)
    # print(arr, k, pivot, end=' ')
    # trivial case
    if (len(arr) == 1) and (arr[0] != k):
        return None
    if (len(arr) == 1) and (arr[0] == k):
        return pivot
    if arr[0] == k:
        return pivot
    # divide
    middle = int(len(arr) / 2)
    if arr[middle] == k:  # if middle is the one we're looking for
        return middle + pivot
    # recursion
    if arr[0] > k and arr[middle] < k:
        return binarySearch(arr[middle:], k, pivot + middle)
    if arr[0] < k and arr[middle] > k:
        return binarySearch(arr[0:middle], k, pivot)
    if arr[0] > k and arr[middle] > k:
        if arr[0] > arr[middle]:
            return binarySearch(arr[0:middle], k, pivot)
        return binarySearch(arr[middle:], k, pivot + middle)
    if arr[0] < k and arr[middle] < k:
        if arr[0] > arr[middle]:
            return binarySearch(arr[0:middle], k, pivot)
        return binarySearch(arr[middle:], k, pivot + middle)


def findIndex(arr, k):
    # input: array 'arr' as unknownly-rotated sorted array & target int 'k'
    # output: index of k in arr
    index = binarySearch(arr, k, 0)
    return index


def findIndex_test(arr, k):
    print(arr, k, "~>", findIndex(arr, k))


if __name__ == "__main__":
    findIndex_test([13, 18, 25, 2, 8, 10], 8)  # return 4
    findIndex_test([13, 18, 25, 2, 8, 10], 13)  # return 0
    findIndex_test([13, 18, 25, 2, 8, 10], 10)  # return 5
    findIndex_test([13, 18, 25, 2, 8, 10], 18)  # return 1
    findIndex_test([13, 18, 25, 2, 8, 10], 25)  # return 2
    findIndex_test([13, 18, 25, 2, 8, 10], 2)  # return 3
    findIndex_test([13, 18, 25, 2, 8, 10], 0)  # return None
    findIndex_test([10, 1, 2, 3], 1)  # return 1
    findIndex_test([2, 3, 10, 1], 1)  # return 3
    findIndex_test([1], 1)  # return 0
    findIndex_test([1], 3)  # return None
