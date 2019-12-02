# ---------------------------
# Author: Tuan Nguyen
# Date created: 20191202
#!203.py
# ---------------------------
"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand. 
Find the minimum element in O(log N) time. You may assume the array does not contain duplicates.

For example, given [5, 7, 10, 3, 4], return 3.
"""

def min_element(arr):
    """ return the min element in O(log N) time from a non-duplicate sorted rotated array """
    n = len(arr)
    if n == 0:      # trivial cases
        return 0
    elif n == 1:
        return arr[0]
    elif n == 2:
        return arr[0] if arr[0] < arr[1] else arr[1]
    else:           # divide-and-conquer
        mid = n // 2   
        left_to_mid = mid - 1
        right_to_mid = mid + 1
        if arr[mid] < arr[left_to_mid] and arr[mid] < arr[right_to_mid]:    # min element is in middle
            return arr[mid]
        elif arr[mid] < arr[-1]:                # middle element is smaller than last element
            return min_element(arr[:mid])       # recursion in half-left part
        else:
            return min_element(arr[mid + 1:])   # else, recursion in half-right part


def test_min_element():
    assert min_element([3, 4, 5, 7, 10]) == 3
    assert min_element([4, 5, 7, 10, 3]) == 3
    assert min_element([5, 7, 10, 3, 4]) == 3
    assert min_element([7, 10, 3, 4, 5]) == 3
    assert min_element([10, 3, 4, 5, 7]) == 3


if __name__ == "__main__":
    test_min_element()
