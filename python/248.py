# ----------------------------
# Author: Tuan Nguyen
# Date created: 20200116
#!248.py
# ----------------------------
"""
Find the maximum of two numbers without using any if-else statements, branching, or direct comparisons.
"""

def find_max(a, b):
    """ return bigger number from a & b without using i-else, branch, direct comparison """
    # imagine 2 sticks of length a and b (a > b), then a + b + |a - b| is exactly 2 times of stick of length a
    # the algorithm works the same for negative a and/or b
    return (a + b + abs(a - b)) / 2.

def test_find_max():
    assert find_max(1, 3) == 3
    assert find_max(3, 10) == 10
    assert find_max(0, 5) == 5
    assert find_max(-5, 10) == 10
    assert find_max(-10, -3) == -3

if __name__ == "__main__":
    test_find_max()