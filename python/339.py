# ----------------------------
# Author: Tuan Nguyen
# Date created: 20200416
#!339.py
# ----------------------------
"""
Given an array of numbers and a number k, 
determine if there are three entries in the array which add up to the specified number k. 
For example, given [20, 303, 3, 4, 25] and k = 49, return true as 20 + 4 + 25 = 49.
"""
def is_summable_three(arr, k):
    """ return True if any 3 elements in unsorted array sum to k; otherwise, return False """
    n = len(arr)
    arr_sorted = sorted(arr)
    for i in range(n-2):
        if is_summable_two_sorted(arr_sorted[i+1:], k - arr_sorted[i]):
            return True
    return False

def is_summable_two_sorted(arr, k):
    """ return True if any 2 element in the sorted input array sum to k; otherwise, return False"""
    n = len(arr)
    l, r = 0, n-1
    while l < r:
        if arr[l] + arr[r] == k:
            return True
        elif arr[l] + arr[r] < k:
            l += 1
        else:
            r -= 1
    return False

# ----- test -----
def test1():
    assert is_summable_three([20, 303, 3, 4, 25], 49) == True

def test2():
    assert is_summable_three([20, 303, 3, 4, 25], 0) == False

if __name__ == "__main__":
    test1()
    test2()