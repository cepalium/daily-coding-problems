# -------------------------------
# Author: Tuan Nguyen
# Date: 20190527
# %14.py
# -------------------------------
"""
The area of a circle is defined as π*r^2. 
Estimate π to 3 decimal places using a Monte Carlo method.
"""


# library
import random


def piEstimationByMonteCarloMethod(iterations):
# input: int iterations
# output: estimation of pi to 3 decimals
    numPointsInCircle = 0
    for i in range(iterations):
        # generate random point (x,y) inside unit square
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:    # new point is inside unit circle (r=1)
            numPointsInCircle += 1
    pi = 4 * numPointsInCircle / iterations  # pi estimation by Monte Carlo method
    return round(pi, 3)     # round to 3 decimals


def piEstimationByMonteCarloMethod_test(iterations):
    print(iterations, piEstimationByMonteCarloMethod(iterations))


if __name__ == "__main__":
    piEstimationByMonteCarloMethod_test(iterations=1000000) # return ~3.141