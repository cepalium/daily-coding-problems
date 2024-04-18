# ------------------------------
# Author: Tuan Nguyen
# Date created: 20200112
#!214.py
# ------------------------------
"""
Given an integer n, return the length of the longest consecutive run of 1s in its binary representation.

For example, given 156, you should return 3.
"""


def longest_consecutive_1(n):
    """return the length of the longest consecutive run of 1s in n's binary representation"""
    str_bin = bin(n)[2:]  # get only string of binary conversion
    max_run, cur_run = 0, 0
    for i in str_bin:
        if i == "1":
            cur_run += 1
        else:
            max_run = cur_run if cur_run > max_run else max_run
            cur_run = 0
    return max_run


def test_longest_consecutive_1():
    assert longest_consecutive_1(156) == 3


if __name__ == "__main__":
    test_longest_consecutive_1()
