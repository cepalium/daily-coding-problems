# -----------------------------------
# Author: Tuan Nguyen
# Date: 20190627
#!solutions/45.py
# -----------------------------------
"""
Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability, 
implement a function rand7() that returns an integer from 1 to 7 (inclusive).
"""

import random

def rand5():
# output: uniformly random int [1,5]
    return random.randint(1, 5)


def rand7():
# output: uniformly random int [1,7] by using rand5()
# method: rand7 = ((rand5 + 5*rand5) % 7) + 1
# condition: rand5 + 5*rand5 < 27
    c = -1  # init c
    while (c >= 27) or (c == -1):
        a = rand5()
        b = rand5() 
        c = a + 5*b
    return (c % 7) + 1  # c % 7 = {0,...6} ~> +1 to have {1,...,7}


def check_uniform_rand7():
# generate rand7() values & print percentage of frequency [1,7]
# if uniform ~> percentages are equal
    freq = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}   # init frequency dictionary
    iterations = 10000  # init number of iterations
    for _ in range(iterations):  # random [1,7] for each iteration and increase its frequency
        r = rand7()
        freq[r] += 1
    # calculate and print the frequency percentage of each element [1,7]
    for k, v in freq.items():
        pct = v * 100.0 / iterations
        print(k, pct)

if __name__ == "__main__":
    check_uniform_rand7()   # print percentage[1,7] ~ 14.286