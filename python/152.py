# ----------------------------
# Author: Tuan Nguyen
# Date created: 20191012
#!solutions/152.py
# ----------------------------
"""
You are given n numbers as well as n probabilities that sum up to 1. 
Write a function to generate one of the numbers with its corresponding probability.

For example, given the numbers [1, 2, 3, 4] and probabilities [0.1, 0.5, 0.2, 0.2], 
your function should return 1 10% of the time, 2 50% of the time, and 3 and 4 20% of the time.

You can generate random numbers between 0 and 1 uniformly.
"""

import random


class CustomizedRandom:
    """constructor"""

    def __init__(self, numbers, prob):
        assert len(numbers) == len(prob)
        n = len(numbers)
        self.pdf = {}  # map PDF initialized {number: max pdf}
        for i in range(n):
            if i == 0:
                self.pdf[numbers[i]] = prob[i]
            else:
                self.pdf[numbers[i]] = prob[i] + self.pdf[numbers[i - 1]]

    """ generate one number from numbers with corresponding probability """

    def random(self):
        r = random.uniform(0, 1)
        for k, v in self.pdf.items():
            if r <= v:
                return k


def customRandom_test(numbers, prob):
    print("numbers={}, prob={}".format(numbers, prob))
    randomGenerator = CustomizedRandom(numbers, prob)
    iterations = 10000
    freq = {i: 0 for i in numbers}  # frequency of each numbers initialized
    for i in range(iterations):
        r = randomGenerator.random()
        freq[r] += 1
    for k, v in freq.items():
        print("{}: {}".format(k, v / iterations))


if __name__ == "__main__":
    customRandom_test(numbers=[1, 2, 3, 4], prob=[0.1, 0.5, 0.2, 0.2])
    customRandom_test(numbers=[1, 2, 3, 4], prob=[0.25, 0.25, 0.25, 0.25])
