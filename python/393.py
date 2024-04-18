# --------------------------
# Author: Tuan Nguyen
# Date created: 20200609
#!393.py
# --------------------------
"""
Given an array of integers, return the largest range, inclusive, of integers that are all included in the array.

For example, given the array [9, 6, 1, 3, 8, 10, 12, 11], return (8, 12) since 8, 9, 10, 11, and 12 are all in the array.
"""


def largest_range(arr):
    n = len(arr)
    if n == 0:
        return (-1, -1)
    sorted_arr = sorted(arr)
    max_len, cur_len = 1, 1
    max_start, max_end, cur_start, cur_end = 0, 0, 0, 0
    for i in range(1, n):
        if sorted_arr[i] == sorted_arr[i - 1] + 1:  # check consecutive
            cur_len += 1
            cur_end += 1
        else:
            cur_len = 1
            cur_start, cur_end = i, i
        if cur_len > max_len:  # update largest range
            max_start = cur_start
            max_end = cur_end
    return (sorted_arr[max_start], sorted_arr[max_end])


def test1():
    assert largest_range([9, 6, 1, 3, 8, 10, 12, 11]) == (8, 12)


def test2():
    assert largest_range([9, 6, 1, 3, 8, 10, 12]) == (8, 10)


def test3():
    assert largest_range([9, 5, 1, 3, 7, 0, -1]) == (-1, 1)


if __name__ == "__main__":
    test1()
    test2()
    test3()
