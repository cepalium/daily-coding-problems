# -----------------------------
# Author: Tuan Nguyen
# Date created: 20190822
#!solutions/101.py
# -----------------------------
"""
Given an even number (greater than 2), return two prime numbers whose sum will be equal to the given number.

A solution will always exist. See Goldbach’s conjecture.

Example:
Input: 4
Output: 2 + 2 = 4

If there are more than one solution possible, return the lexicographically smaller solution.
If [a, b] is one solution with a <= b, and [c, d] is another solution with c <= d, 
then [a, b] < [c, d] if a < c OR a==c AND b < d.
"""

import random


def isPrime(N):
    # input: int N >=2
    # output: True if N is prime, False if N is composite
    # method: Fermat's primality test
    # running time: O(n^3)
    if N == 1:
        return False
    if (N == 2) or (N == 3):
        return True
    a = random.randint(2, N - 1)
    b = a ** (N - 1) % N
    if b != 1:
        return False
    return True


def goldbachConjecture(n):
    # input: int n >= 2
    # output: list [a,b]; a & b prime s.t a+b=n
    goldbachPair = []  # output declared
    a = 2  # int a initialized
    while a <= n / 2:  # loop until a = n/2
        if not isPrime(a):
            a += 1
            continue
        b = n - a
        if not isPrime(b):
            a += 1
            continue
        goldbachPair = [a, b]  # both a & b are primes and a+b=n
        break
    return goldbachPair


def goldbachConjecture_test(n):
    print(n, "~>", goldbachConjecture(n))


if __name__ == "__main__":
    for i in range(4, 10):
        goldbachConjecture_test(i)
