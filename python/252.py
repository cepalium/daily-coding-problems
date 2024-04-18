# ---------------------------
# Author: Tuan Nguyen
# Date created: 20200120
#!252.py
# ---------------------------
"""
The ancient Egyptians used to express fractions as a sum of several terms where each numerator is one. 
For example, 4 / 13 can be represented as 1 / 4 + 1 / 18 + 1 / 468.

Create an algorithm to turn an ordinary fraction a / b, where a < b, into an Egyptian fraction.
"""
import math


def egyptian_fraction(n, d):
    """return sring of Egyptian fraction from input fraction n / d"""
    denoms = []  # list store all denominators
    while n != 0:
        x = math.ceil(d / n)  # possible denominator
        denoms.append(x)
        n = (
            n * x - d
        )  # update nominator & denominator after extracting 1 Eygyptian fraction
        d = d * x
    str_denoms = ["1 / " + str(den) for den in denoms]
    return " + ".join(str_denoms)


def test_egyptian_fraction():
    assert egyptian_fraction(4, 13) == "1 / 4 + 1 / 18 + 1 / 468"


if __name__ == "__main__":
    test_egyptian_fraction()
