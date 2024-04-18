# ----------------------------------
# Author: Tuan Nguyen
# Date created: 20200520
#!373.py
# ----------------------------------
"""
Given a list of integers L, find the maximum length of a sequence 
of consecutive numbers that can be formed using elements from L.

For example, given L = [5, 2, 99, 3, 4, 1, 100], 
return 5 as we can build a sequence [1, 2, 3, 4, 5] which has length 5.
"""


def max_length_consecutive_number_sequence(arr):
    n = len(arr)
    if n == 0:  # trivial cases
        return 0
    if n == 1:
        return 1
    # initialize s: i-th number in s indicates the max length
    # of consecutive number corresponding to i-th number in input array
    s = [None for i in range(n)]
    arr = sorted(arr)
    s[0] = 1  # base case
    for i in range(1, n):  # dynamic programming
        if arr[i] == arr[i - 1] + 1:  # bellman's equation
            s[i] = s[i - 1] + 1
        else:
            s[i] = 1
    return max(s)


def test1():
    assert max_length_consecutive_number_sequence([]) == 0


def test2():
    assert max_length_consecutive_number_sequence([10]) == 1


def test3():
    assert (
        max_length_consecutive_number_sequence([5, 2, 99, 3, 4, 1, 100]) == 5
    )


def test4():
    assert (
        max_length_consecutive_number_sequence([5, 2, 99, -3, 4, 1, 100]) == 2
    )


def test5():
    assert (
        max_length_consecutive_number_sequence([-5, -2, 99, -3, -4, -1, 100])
        == 5
    )


if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()
