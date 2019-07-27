# -------------------------------------
# Author: Tuan Nguyen
# Date: 20190727
#!solutions/75.py
# -------------------------------------
"""
Given an array of numbers, find the length of the longest increasing subsequence in the array. 
The subsequence does not necessarily have to be contiguous.

For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], 
the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.
"""

def longestIncreasingSubsequence(arr):
# input: array arr
# output: length of longest increasing subsequence in arr
    s = []
    # base case:
    s.append(1) # s[0] = 1
    # recursion
    for i in range(1, len(arr)):
        tmp = [s[j] for j in range(len(s)) if arr[j] < arr[i]]  # list {s[j] | j < i, arr[j] < arr[i]}
        tmp.append(0)   # list {0, s[j] | j < i, arr[j] < arr[i]}
        s_i = 1 + max(tmp)  # Bellman's equation: s[i] = 1 + max(0, s[j] | j < i, arr[j < arr[i]])
        s.append(s_i)
    return max(s)


def longestIncreasingSubsequence_test(arr):
    print(arr, '~>', longestIncreasingSubsequence(arr))


if __name__ == "__main__":
    longestIncreasingSubsequence_test([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15])   # return 6