# --------------------------
# Author: Tuan Nguyen
# Date created: 20191024
#!164.py
# --------------------------
"""
You are given an array of length n + 1 whose elements belong to the set {1, 2, ..., n}. 
By the pigeonhole principle, there must be a duplicate. Find it in linear time and space.
"""


def duplicate(arr):
    """find the duplicate in an array of length n + 1 whose elements belong to the set {1, 2, ..., n}"""
    n = len(arr) - 1  # the max element in array
    expected_sum = n * (n + 1) / 2
    array_sum = sum(arr)
    return array_sum - expected_sum


def test_duplicate():
    assert duplicate([1, 1, 2, 3]) == 1
    assert duplicate([1, 2, 3, 4, 5, 5, 6, 7, 8, 9]) == 5
    assert duplicate([1, 2, 3, 3, 4, 5, 6]) == 3


if __name__ == "__main__":
    test_duplicate()
