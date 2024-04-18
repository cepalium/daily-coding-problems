# -----------------------------
# Author: Tuan Nguyen
# Date created: 20190912
#!solutions/96.py
# -----------------------------
"""
Given a number in the form of a list of digits, return all possible permutations.

For example, given [1,2,3], return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].
"""

import itertools


def permutations(li):
    # input: list of digits
    # output: all possible permutations from input list
    # method: itertools.permutations
    return list(itertools.permutations(li))


def permutations_test(li):
    print("Input list: {}\nPermutations: {}".format(li, permutations(li)))


if __name__ == "__main__":
    permutations_test([1, 2, 3])
