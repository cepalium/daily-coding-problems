# ---------------------------------
# Author: Tuan Nguyen
# Date created: 20200305
#!295.py
# --------------------------------
"""
Pascal's triangle is a triangular array of integers constructed with the following formula:

The first row consists of the number 1.
For each subsequent row, each element is the sum of the numbers directly above it, on either side.
For example, here are the first few rows:

    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
Given an input k, return the kth row of Pascal's triangle.

Bonus: Can you do this using only O(k) space?
"""


def pascal_triangle(n):
    """return n-th row of Pascal's triangle"""
    # trivial cases
    if n < 1:
        return []
    if n == 1:
        return [1]
    # factorial list
    fact = [1 for i in range(n)]  # O(n) space
    for i in range(1, n):
        fact[i] = fact[i - 1] * i  # factorial in O(n) time
    # pascal triangle line n
    pascal = [1 for i in range(n)]  # O(n) space
    for i in range(n):
        pascal[i] = fact[n - 1] // (
            fact[i] * fact[n - i - 1]
        )  # pascal in O(n) time
    return pascal


def test1():
    assert pascal_triangle(0) == []


def test2():
    assert pascal_triangle(1) == [1]


def test3():
    assert pascal_triangle(2) == [1, 1]


def test4():
    assert pascal_triangle(3) == [1, 2, 1]


def test5():
    assert pascal_triangle(4) == [1, 3, 3, 1]


def test6():
    assert pascal_triangle(5) == [1, 4, 6, 4, 1]


if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
