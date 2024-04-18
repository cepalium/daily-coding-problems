# ------------------------------
# Author: Tuan Nguyen
# Date: 20190723
#!solutions/71.py
# ------------------------------
"""
Using a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform probability, 
implement a function rand5() that returns an integer from 1 to 5 (inclusive).
"""

import random


def rand7():
    # output: a uniformly random int in range [1, 7]
    return random.randint(1, 7)


def rand5():
    # output: a uniformly random int in range [1, 5]
    # requirements: build rand5() from rand7()
    # method: [ ( rand7 + 7*rand7 ) mod 5 ] + 1
    # condition: rand7 + 7*rand7 < 53
    c = rand7() + 7 * rand7()  # c = {8,9,10,...,56}
    while c >= 53:
        c = rand7() + 7 * rand7()
    return (c % 5) + 1  # c % 5 = {0,1,...,4} => (c % 5) + 1 = {1,2,...,5}


def check_uniform_rand5():
    freq = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    iterations = 10000
    for _ in range(iterations):
        r = rand5()
        freq[r] += 1
    for k, v in freq.items():
        print(k, v / iterations)


if __name__ == "__main__":
    check_uniform_rand5()
