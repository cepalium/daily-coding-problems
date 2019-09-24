# ---------------------------
# Author: Tuan Nguyen
# Date created: 20190924
#!solutions/129.py
# ---------------------------
"""
Given a real number n, find the square root of n. For example, given n = 9, return 3.
"""

def squareRoot(n):
# input: a real number n
# output: square root of n round to 3 decimals
# method: newton's approximation x_1 = x_0 - f(x_0)/f'(x_0)
# f(x) = x^2 - n, f'(x) = 2x
    # instance variables initialized
    x1 = 0      # start x1 from 0
    x0 = 1      # start x0 from 1 ~> avoid nominator to be 0 (DivideByZero exception)
    while True:
        x1 = x0 - (x0**2 - n) / (2*x0)      # newton's approximation formular to find square root
        if round(x1, 3) == round(x0, 3):    # if the approximation is accurate to 3 decimals
            break                           # then break
        x0 = x1                             # else, continue the approximation by updating x0
    return round(x1, 3)


def squareRoot_test(n, desiredVal):
    print("sqrt({})={}, test={}".format(n, squareRoot(n), squareRoot(n)==desiredVal))


if __name__ == "__main__":
    squareRoot_test(9, 3)
    squareRoot_test(2, 1.414)