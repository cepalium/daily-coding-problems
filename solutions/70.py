# -------------------------------
# Author: Tuan Nguyen
# Date: 20190722
#!solutions/70.py
# -------------------------------
"""
A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.
"""

def nthPerfectNumber(n):
# input: int n
# output: n-th perfect number
# perfect number := sum all digits equals to 10
    # init
    pNumber = 0
    n0 = 0
    # loop: 
    while n0 < n:
        pNumber += 1
        sum_digits_in_pNumber = sum([int(d) for d in str(pNumber)])
        if sum_digits_in_pNumber <= 10: # increase n0 only if possible to construct perfect number from pNumber
            n0 += 1
    return int(str(pNumber) + str(10 - sum_digits_in_pNumber))


def nthPerfectNumber_test(n):
    print("{0}-th perfect number: {1}".format(n, nthPerfectNumber(n)))


if __name__ == "__main__":
    for i in range(1, 51):
        nthPerfectNumber_test(i)