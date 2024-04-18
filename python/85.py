# -------------------------------
# Author: Tuan Nguyen
# Date: 20190807
#!solutions/85.py
# -------------------------------
"""
Given three 32-bit integers x, y, and b, 
return x if b is 1 and y if b is 0, using only mathematical or bit operations. 
You can assume b can only be 1 or 0.
"""


def xOrY(x, y, b):
    # input: 3 ints x, y, b; b={0,1}
    # output: x if b=1, y if b=0
    # method: output = x*b + y*|b-1|
    return x * b + y * abs(b - 1)


def xOrY_test(x, y, b):
    print("x={}, y={}, b={} ~> output: {}".format(x, y, b, xOrY(x, y, b)))


if __name__ == "__main__":
    xOrY_test(5, 10, 1)  # return 5
    xOrY_test(5, 10, 0)  # return 10
