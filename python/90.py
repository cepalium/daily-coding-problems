# ----------------------------
# Author: Tuan Nguyen
# Date: 20190812
#!solutions/90.py
# ----------------------------
"""
Given an integer n and a list of integers l, 
write a function that randomly generates a number from 0 to n-1 that isn't in l (uniform).
"""

import random


def randomNotInList(n, l):
    # input: int n & list of integers l
    # output: a uniformly-random integer [0, n-1] s.t it is not in l
    r = random.randint(0, n - 1)
    while r in l:
        r = random.randint(0, n - 1)
    return r


def random_test():
    # task: generate random numbers & calculate their probabilities
    n = 10  # n initialized
    l = [
        i for i in range(n) if i % 2 == 0
    ]  # list l initialized: all even integers < n
    freq = {
        i: 0 for i in range(n) if i not in l
    }  # dict freq initialized: frequency of each possible output
    iterations = 10000  # no. iterations initialized
    # loop: generate random number & keep track of its frequency
    for _ in range(iterations):
        r = randomNotInList(n, l)
        freq[r] += 1
    # print the probability of each random int
    # if all probabilities are approximately equal, then random method is uniform
    for k, v in freq.items():
        print("{}: {}".format(k, v / iterations))


if __name__ == "__main__":
    random_test()
