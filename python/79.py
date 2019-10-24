# ------------------------------
# Author: Tuan Nguyen
# Date: 20190731
#!solutions/79.py
# ------------------------------
"""
Given an array of integers, write a function to determine whether the array could become non-decreasing by modifying at most 1 element.

For example, given the array [10, 5, 7], you should return true, since we can modify the 10 into a 1 to make the array non-decreasing.

Given the array [10, 5, 1], you should return false, since we can't modify any one element to get a non-decreasing array.
"""

def is_nonDecreasing(arr, m):
# input: array of ints 'arr' & int m as max no. element modifications
# output: True/False if arr is non-decreasing with at most m element modifications
    # trivial case: array has 0 or 1 element ~> always True
    if len(arr) < 2:
        return True
    # iteration
    for i in range(1, len(arr)):
        # 2 adjacent elements are non-decreasing ~> continue
        if arr[i] > arr[i-1]:   
            continue
        # else: 2 adjacent elements are NOT non-decreasing
        # false case 1: 2 elements are NOT non-decreasing & no modification left
        if m == 0:
            return False
        # 2 elements are NOT non-decreasing & can modify element if possible
        prevElement_digits = [int(d) for d in str(arr[i-1])]
        # false case 2: 2 adjacent elements are NOT non-decreasing & no possible modification
        if arr[i] < min(prevElement_digits): 
            return False
        # else: 2 adjacent elements are NOT non-decreasing & a modification is possible
        m -= 1  # decrease no. modifications, then continue
    return True


def nonDecreasing_test(arr, m):
    print(arr, '~>', is_nonDecreasing(arr, m))


if __name__ == "__main__":
    nonDecreasing_test([10, 5, 7], 1)  # return True
    nonDecreasing_test([10, 5, 1], 1)  # return False
    nonDecreasing_test([10], 1)  # return True
    nonDecreasing_test([0, 5, 1], 1)  # return False