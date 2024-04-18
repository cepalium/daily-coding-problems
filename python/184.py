# --------------------------
# Author: Tuan Nguyen
# Date created: 20191114
#!184.py
# --------------------------
"""
Given n numbers, find the greatest common denominator between them.

For example, given the numbers [42, 56, 14], return 14.
"""


def gcd_from_list(lst):
    """return the greatest common denominator between n numbers"""
    if len(lst) == 0:  # trivial case
        return -1
    while len(lst) > 1:
        a = lst.pop()
        b = lst.pop()
        c = gcd(a, b) if a >= b else gcd(b, a)
        lst.append(c)
    return lst.pop()


def gcd(a, b):
    """return the greatest coomon denominator between a & b, a>=b"""
    if a < b:
        raise ValueError("a must be larger than b")
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def test_gcdList():
    assert gcd_from_list([42, 56, 14]) == 14
    assert gcd_from_list([3, 6]) == 3
    assert gcd_from_list([1]) == 1
    assert gcd_from_list([]) == -1


if __name__ == "__main__":
    test_gcdList()
