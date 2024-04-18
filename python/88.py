# --------------------------------
# Author: Tuan Nguyen
# Date: 20190810
#!solutions/88.py
# --------------------------------
"""
Implement division of two positive integers without using the division, multiplication, or modulus operators. 
Return the quotient as an integer, ignoring the remainder.
"""


def division(a, b):
    # input: 2 ints a & b; a>0, b>0
    # output: int q = a/b, ignoring r
    q = 0
    while b <= a:
        a = a - b
        q += 1
    return q


def division_test(a, b):
    print("{} / {} = {}".format(a, b, division(a, b)))


if __name__ == "__main__":
    division_test(10, 5)  # return 2
    division_test(9, 3)  # return 3
    division_test(9, 4)  # return 2
    division_test(1, 5)  # return 0
