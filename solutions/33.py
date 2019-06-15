# ------------------------------------
# Author: Tuan Nguyen
# Date: 20190615
#!solutions/33.py
# ------------------------------------
"""
Compute the running median of a sequence of numbers. 
That is, given a stream of numbers, print out the median of the list so far on each new element.
Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:
2
1.5
2
3.5
2
2
2
"""

import random


def merge(A, B):
# input: 2 sorted lists A & B of ints
# output: list C merged from all elements of A & B ascendingly
    C = []  # init merged list, i.e output list
    i = 0
    j = 0
    # compare and merge A & B 
    while (i < len(A)) and (j < len(B)):
        if A[i] <= B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    # in case A | B has been merged all -> copy the rest of the other list into C
    while i < len(A):
        C.append(A[i])
        i += 1
    while j < len(B):
        C.append(B[j])
        j += 1
    return C


def mergeSort(arr):
# input: list arr of ints
# output: sorted list arr
    # trivial case
    if len(arr) <= 1:
        return arr
    # recursion
    lArr = mergeSort(arr[:int(len(arr) / 2)])   # sort half left of arr
    rArr = mergeSort(arr[int(len(arr) / 2):])   # sort half right of arr
    # combine
    arr = merge(lArr, rArr)
    return arr


def findMedian(arr):
# input: list arr of ints
# output: median of arr
# method: mergesort -> pick median
    # init median index
    if len(arr) % 2 != 0:   # odd-numbered list
        k1 = k2 = int(len(arr) / 2) # median index in middle
    else:   # even-numbered list
        k1 = int(len(arr) / 2) - 1  # left middle index
        k2 = k1 + 1                 # right middle index
    # sort arr
    arr = mergeSort(arr)
    # calculate median
    median = (arr[k1] + arr[k2]) / 2
    return median


def printMedianOfSequence(seq):
# input: list seq of ints
# output: print median of list so far on each new element
    for i in range(1, len(seq) + 1):
        print(seq[:i], "-> Median: ", findMedian(seq[:i]))


if __name__ == "__main__":
    printMedianOfSequence([2, 1, 5, 7, 2, 0, 5])  # print 2, 1.5, 2, 3.5, 2, 2, 2