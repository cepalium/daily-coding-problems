# ----------------------------
# Author: Tuan Nguyen
# Date: 20190718
#!solutions/66.py
# ----------------------------
"""
Assume you have access to a function toss_biased() 
which returns 0 or 1 with a probability that's not 50-50 (but also not 0-100 or 100-0). 
You do not know the bias of the coin.

Write a function to simulate an unbiased coin toss.
"""

import random

biased_rate = 0.7


def toss_biased():
    # output: 0/1 but the probability of 0/1 will be biased by 'biased_rate'
    return int(
        random.random() < biased_rate
    )  # prob(1) = biased_rate, prob(0) = 1 - biased_rate


def toss_unbiased():
    # output: 0/1 and the probability of 0/1 is equal, i.e 50%
    # method: von Neumann's unbiased toss from biased toss
    # toss 2 times: if (0, 1), then return 0; if (1,0), then return 1; else, toss 2 times again
    toss1 = toss_biased()
    toss2 = toss_biased()
    while toss1 == toss2:  # toss again if (toss1, toss2) = (0,0) or (1,1)
        toss1 = toss_biased()
        toss2 = toss_biased()
    # only continue if toss1 != toss2
    if (toss1 == 0) and (toss2 == 1):  # (toss1, toss2) = (0,1) ~> 0
        return 0
    return 1  # (toss1, toss2) = (1,0) ~> 1


def main():
    # init
    iterations = 10000  # no. iterations
    bias = {
        0: 0,
        1: 0,
    }  # dict of toss_biased(): frequencies of 0 and 1 separately
    unbias = {
        0: 0,
        1: 0,
    }  # dict of toss_unbiased: frequencies of 0 and 1 separately
    for _ in range(iterations):
        # toss
        biased_trial = toss_biased()
        unbiased_trial = toss_unbiased()
        # increase frequencies
        bias[biased_trial] += 1
        unbias[unbiased_trial] += 1
    # print results
    print("Biased rate:", biased_rate)
    print("Bias:\t0 ~>", bias[0] / iterations, ";\t1 ~>", bias[1] / iterations)
    print(
        "Unbias:\t0 ~>",
        unbias[0] / iterations,
        ";\t1 ~>",
        unbias[1] / iterations,
    )


if __name__ == "__main__":
    main()
