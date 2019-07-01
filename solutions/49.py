# ------------------------------------
# Author: Tuan Nguyen
# Date: 20190701
#!solutions/49.py
# ------------------------------------
"""
Given an array of numbers, 
find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], 
the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, 
since we would not take any elements.

Do this in O(N) time.
"""

def contiguousSubarrayMaxSum(a):
# input: list 'a' of ints
# output: max sum of contiguous subarray of 'a'
# method: dynamic programming
# running time: O(n)
    maxSum = 0  # init output as 0
    # base case
    S = [a[0]]   # init list storing temporary maxSum with arr[0] as 1st element
    # iteration
    for i in range(1, len(a)):
        S.append(max(a[i], S[i-1] + a[i]))  # Bellman's equation: s[i] = max(a[i], s[i-1] + a[i])
    for s in S[1:]: # only consider the 2nd element to end of S b/c we need maxSum of contiguous subarray ~> contiguous: > 1 element
        maxSum = s if s > maxSum else maxSum
    return maxSum


def contiguousSubarrayMaxSum_test(arr):
    print(arr, '~> maxSum:', contiguousSubarrayMaxSum(arr))


if __name__ == "__main__":
    contiguousSubarrayMaxSum_test([34, -50, 42, 14, -5, 86])    # return 137
    contiguousSubarrayMaxSum_test([-5, -1, -8, -9]) # return 0