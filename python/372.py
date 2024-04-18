# -------------------------------
# Author: Tuan Nguyen
# Date created: 20200519
#!372.py
# -------------------------------
"""
Write a function that takes a natural number as input and returns the number of digits the input has.

Constraint: don't use any loops.
"""


def count_digits(number, count=0):
    if number <= 0:
        raise Exception("Input number must be positive")
    if number < 10:
        return count + 1
    return count_digits(number // 10, count + 1)


def test1():
    assert count_digits(1) == 1


def test2():
    assert count_digits(100) == 3


def test3():
    assert count_digits(9999) == 4


if __name__ == "__main__":
    test1()
    test2()
