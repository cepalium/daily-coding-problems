# -------------------------
# Author: Tuan Nguyen
# Date created: 20200102
#!233.py
# -------------------------
"""
Implement the function fib(n), which returns the nth number in the Fibonacci sequence, 
using only O(1) space.
"""

def fib(n):
    """ return nth number in Fibonacci sequence """
    if n == 0:      # trivial cases
        return 0
    elif n == 1:
        return 1
    else:           # non-trivial
        f_1, f_2 = 1, 0             # initialize: f_n-1 & f_n-2
        for i in range(2, n+1):     # iteratively calculate nth Fibonacci number
            temp = f_1
            f_1 = f_1 + f_2         # f_n = f_n-1 + f_n-2
            f_2 = temp
        return f_1


def test_fib():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3


if __name__ == "__main__":
    test_fib()