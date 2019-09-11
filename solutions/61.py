# -------------------------
# Author: Tuan Nguyen
# Date created: 20190911
#!solutions/61.py
# -------------------------
"""
Implement integer exponentiation. 
That is, implement the pow(x, y) function, where x and y are integers and returns x^y.

Do this faster than the naive method of repeated multiplication.

For example, pow(2, 10) should return 1024.
"""

def pow(x, y):
# input: 2 ints x & y
# output: returns x^y
# method: recursion: x^y = (x^2) ^ (y//2) if y even; else x^y = [(x^2)*x]^(y//2) 
    if y == 1:  # base case
        return x
    z = pow(x*x, y//2)  # recur: square x, halve y
    if y % 2 == 1:  # if y is odd
        z = z*x
    return z


def pow_test(x, y):
    print("{}^{} = {}".format(x, y, pow(x, y)))


if __name__ == "__main__":
    pow_test(2, 10) # print 1024
    pow_test(3, 3)  # print 27