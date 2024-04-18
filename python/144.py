# ---------------------------
# Author: Tuan Nguyen
# Date created: 20191004
#!solutions/144.py
# ---------------------------
"""
Given an array of numbers and an index i, return the index of the nearest larger number of the number at index i, 
where distance is measured in array indices.

For example, given [4, 1, 3, 5, 6] and index 0, you should return 3.

If two distances to larger numbers are the equal, then return any one of them. 
If the array at i doesn't have a nearest larger integer, then return null.

Follow-up: If you can preprocess the array, can you do this in constant time?
"""

import math


def successorDistance(array, i):
    # input: array of numbers and index i
    # output: index of nearest larger number of number at index i
    n = len(array)
    if i >= n or i < 0:
        raise IndexError("Invalid index: " + str(i))
    successor = math.inf  # sucessor initialized to inf
    d = math.inf  # sucessor index initailized to inf
    mark = array[i]
    for j in range(n):
        if (
            array[j] > mark and array[j] < successor
        ):  # the current number is the nearest larger number
            d = j  # update successor index
            successor = array[j]  # update successor
    if d == math.inf:  # cannot find the successor
        return None
    return d  # if reach this, then a successor found successfylly


def successorDistance_test(array, i, desiredVal):
    print(successorDistance(array, i) == desiredVal)


if __name__ == "__main__":
    successorDistance_test(array=[4, 1, 3, 5, 6], i=0, desiredVal=3)
    successorDistance_test(array=[4, 1, 3, 5, 6], i=1, desiredVal=2)
    successorDistance_test(array=[4, 1, 3, 5, 6], i=2, desiredVal=0)
    successorDistance_test(array=[4, 1, 3, 5, 6], i=3, desiredVal=4)
    successorDistance_test(array=[4, 1, 3, 5, 6], i=4, desiredVal=None)
    successorDistance_test(array=[4, 1, 3, 5, 6], i=5, desiredVal=IndexError)
