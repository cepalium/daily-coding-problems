# ----------------------------
# Author: Tuan Nguyen
# Date created: 20200321
#!311.py
# ----------------------------
"""
Given an unsorted array, in which all elements are distinct, find a "peak" element in O(log N) time.

An element is considered a peak if it is greater than both its left and right neighbors. 
It is guaranteed that the first and last elements are lower than all others.
"""


def find_peak(arr):
    """Return the peak element in an unsorted array with all distinct elements.
    An element is considered a peak if it is greater than both of its left and right neighbors
    """
    # trivial cases
    n = len(arr)
    if n == 0:
        return None
    if n == 1:
        return arr[0]
    if n == 2:
        return max(arr)
    if n == 3:
        return arr[1]
    # n > 3
    return binary_search_peak(arr, 0, n - 1)


def binary_search_peak(arr, left, right):
    """binary search for peak element in array"""
    # trivial cases
    if left == right:
        return arr[left]
    if left > right:
        return None
    # else: left < right
    middle = (left + right) // 2
    if arr[middle - 1] < arr[middle] and arr[middle] > arr[middle + 1]:
        return arr[middle]
    elif arr[middle - 1] < arr[middle] < arr[middle + 1]:
        return binary_search_peak(arr, middle, right)
    else:  # arr[middle-1] > arr[middle] > arr[middle+1]
        return binary_search_peak(arr, left, middle)


# ----- UNIT TESTS -----
def test1():
    assert find_peak([1, 2, 3, 5, 4]) == 5


def test2():
    assert find_peak([]) == None


def test3():
    assert find_peak([1]) == 1


def test4():
    assert find_peak([1, 2]) == 2


def test5():
    assert find_peak([1, 3, 2]) == 3


def test6():
    assert find_peak([1, 5, 4, 3, 2]) == 5


def test7():
    assert find_peak([1, 2, 5, 4, 3]) == 5


if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
