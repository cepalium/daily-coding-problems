# ---------------------------
# Author: Tuan Nguyen
# Date created: 20191008
#!solutions/147.py
# ---------------------------
"""
Given a list, sort it using this method: reverse(lst, i, j), which reverses lst from i to j.
"""


def sortByReverse(arr):
    # input: a list of integers
    # output: a sorted list
    # method: sort by using method 'reverse'
    # running time: O(n^2)
    n = len(arr)
    for i in range(n):  # each iteration reverse the min to first of arr
        curMin = min(
            arr[i:]
        )  # current min element from [arr[i], arr[i+1], ..., arr[n-1]]
        minIndex = arr.index(curMin)  # index of current min
        reverse(arr, i, minIndex)  # reverse current min element to first
    return arr


def reverse(lst, i, j):
    # input: list lst of integers, int i & j as indices in lst
    # task: reverse all elements of lst from i to j
    # trivial case
    if i >= j:
        return lst
    else:
        lst[i], lst[j] = lst[j], lst[i]
        return reverse(lst, i + 1, j - 1)


def reverse_test(lst, desiredVal):
    reversedList = reverse(lst, 0, len(lst) - 1)
    print(reversedList, reversedList == desiredVal)


def sortByReverse_test(arr, desiredVal):
    sortedList = sortByReverse(arr)
    print(sortedList, sortedList == desiredVal)


if __name__ == "__main__":
    # reverse unit test
    reverse_test(lst=[1, 2, 3, 4, 5], desiredVal=[5, 4, 3, 2, 1])
    reverse_test(lst=[], desiredVal=[])
    reverse_test(lst=[1], desiredVal=[1])
    reverse_test(lst=[1, 2], desiredVal=[2, 1])
    reverse_test(lst=[1, 3, 2, 5, 4], desiredVal=[4, 5, 2, 3, 1])
    # sort by reverse unit test
    sortByReverse_test(arr=[1, 2, 3, 4, 5], desiredVal=[1, 2, 3, 4, 5])
    sortByReverse_test(arr=[1], desiredVal=[1])
    sortByReverse_test(arr=[], desiredVal=[])
    sortByReverse_test(arr=[5, 4, 3, 2, 1], desiredVal=[1, 2, 3, 4, 5])
    sortByReverse_test(arr=[3, 1, 2, 5, 4], desiredVal=[1, 2, 3, 4, 5])
