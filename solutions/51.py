# ---------------------------------
# Author: Tuan Nguyen
# Date: 20190703
#!solutions/51.py
# ---------------------------------
"""
Given a function that generates perfectly random numbers between 1 and k (inclusive), where k is an input, 
write a function that shuffles a deck of cards represented as an array using only swaps.

It should run in O(N) time.

Hint: Make sure each one of the 52! permutations of the deck is equally likely.
"""

import random

def randK(k):
# input: int k
# output: random int in range [1, k]
    return random.randint(1, k)


def shuffle(a):
# input: array 'a' of int
# output: shuffled array 
# method: Fisher-Yates shuffle algorithm
    n = len(a)
    for i in range(n - 1, 1, -1):   # loop from n-1 to 1
        j = randK(i)    # j = random int s.t 1 <= j <= i
        a[i], a[j] = a[j], a[i] # swap the random-indexed element to last
    return a


def shuffle_test(a):
    print(a, '~> shuffle:', shuffle(a))


if __name__ == "__main__":
    shuffle_test([1,2,3,4,5,6,7,8,9,10])
