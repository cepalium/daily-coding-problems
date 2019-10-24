# --------------------------------------
# Author: Tuan Nguyen
# Date: 20190712
#!solutions/60.py
# --------------------------------------
"""
Given a multiset of integers, 
return whether it can be partitioned into two subsets whose sums are the same.

For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, 
it would return true, 
since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.

Given the multiset {15, 5, 20, 10, 35}, it would return false, 
since we can't split it up into two subsets that add up to the same sum.
"""

def is_partitioned_sameSum(arr):
# input: list 'arr' of ints
# output: True/False if 'arr' can be partitioned into 2 subsets whose sums are the same
# algorithm: 
# 1. calculate sum of array ~> If sum is odd, then False because impossible to partition into 2 same-sum subsets
# 2. sort array
# 3. loop: subset_sum substract element in array if the left amount >= 0
# after loop, if subset_sum is 0, then True because successfully find 1 subset, else False  
# running time: O(n*logn) b/c sort takes O(n*logn) + loop takes O(n)
    arr_sum = sum(arr)
    # trivial case: sum is odd
    if arr_sum % 2 != 0:
        return False
    subset_sum = arr_sum / 2    # sum of 1 subset = 1/2 sum of array
    # sort array
    sorted_arr = sorted(arr)
    # loop
    for e in sorted_arr:
        if subset_sum - e >= 0:
            subset_sum -= e
    if subset_sum != 0:
        return False
    return True


def is_partitioned_sameSum_test(arr):
    print(arr, '~>', is_partitioned_sameSum(arr))


if __name__ == "__main__":
    is_partitioned_sameSum_test([15, 5, 20, 10, 35, 15, 10])    # return True
    is_partitioned_sameSum_test([15, 5, 20, 10, 35])    # return False