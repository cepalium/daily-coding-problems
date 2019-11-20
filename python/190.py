# --------------------------
# Author: Tuan Nguyen
# Date created: 20191120
#!190.py
# --------------------------
"""
Given a circular array, compute its maximum subarray sum in O(n) time. 
A subarray can be empty, and in this case the sum is 0.

For example, given [8, -1, 3, 4], return 15 as we choose the numbers 3, 4, and 8 
where the 8 is obtained from wrapping around.

Given [-4, 5, 1, 0], return 6 as we choose the numbers 5 and 1.
"""

def max_subarray_sum_naive(arr):
    """ return max subarray sum from a circular array in O(n^2) time """
    best_max = None
    n = len(arr)
    for i in range(n):
        s = arr[i:] + arr[:i]   # rotated array
        current_max = kadane(s)
        if (best_max is None) or (current_max > best_max):
            best_max = current_max
    return best_max


def max_subarray_sum_smart(arr):
    """ return max subarray sum from a curcular array in O(n) time """
    max_kadane = kadane(arr)

    max_wrap = sum(arr) + kadane([-e for e in arr]) # array sum + kadane(invert-positive-negative input array)

    return max_kadane if max_kadane > max_wrap else max_wrap


def kadane(arr):
    """ return max subarray sum in O(n) time """
    n = len(arr)
    if n == 0:      # trivial case
        return 0
    if is_all_negative(arr):
        return max(arr)
    # else
    best_max = None
    current_max = 0
    for e in arr:
        current_max += e
        if current_max < 0:
            current_max = 0
        if (best_max is None) or (current_max > best_max):
            best_max = current_max
    return best_max


def is_all_negative(arr):
    """ return True if all elements in array are negative """
    for e in arr:
        if e >= 0:
            return False
    return True


def test_maxSubarraySum():
    # test 1
    arr = [8, -1, 3, 4]
    assert max_subarray_sum_naive(arr) == 15
    assert max_subarray_sum_smart(arr) == 15
    # test 2
    arr = [-4, 5, 1, 0]
    assert max_subarray_sum_naive(arr) == 6
    assert max_subarray_sum_smart(arr) == 6

if __name__ == "__main__":
    test_maxSubarraySum()