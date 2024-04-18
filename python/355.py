# -----------------------
# Author: Tuan Nguyen
# Date created> 20200502
#!355.py
# -----------------------
"""
You are given an array X of floating-point numbers x1, x2, ... xn. 
These can be rounded up or down to create a corresponding array Y of integers y1, y2, ... yn.

Write an algorithm that finds an appropriate Y array with the following properties:

* The rounded sums of both arrays should be equal.
* The absolute pairwise difference between elements is minimized. 
In other words, |x1- y1| + |x2- y2| + ... + |xn- yn| should be as small as possible.

For example, suppose your input is [1.3, 2.3, 4.4]. 
In this case you cannot do better than [1, 2, 5], 
which has an absolute difference of |1.3 - 1| + |2.3 - 2| + |4.4 - 5| = 1.
"""


def find_Y(X):
    Y_list = find_all_possible_rounded_arrays(X)
    Y_list = find_equal_sum_arrays(X, Y_list)
    Y = get_min_pairwise_absolute_difference_array(X, Y_list)
    return Y  # Y is a set data structure


def find_all_possible_rounded_arrays(X):
    from itertools import product

    rounded_options = []
    for x in X:
        x_rounded = [int(x), int(x) + 1]
        rounded_options.append(x_rounded)
    Y_list = list(
        product(*rounded_options)
    )  # treat all elements in rounded_options as *args for product()
    return Y_list  # a list of sets


def find_equal_sum_arrays(X, Y_list):
    equal_sum_arrays = []
    sum_X = sum(X)
    for Y in Y_list:
        sum_Y = sum(Y)
        if sum_Y == sum_X:
            equal_sum_arrays.append(Y)
    return equal_sum_arrays


def get_min_pairwise_absolute_difference_array(X, Y_list):
    min_diff = calculate_pairwise_absolute_difference(X, Y_list[0])
    min_arr = Y_list[
        0
    ]  # initialized the min array with 1st element from all options
    for Y in Y_list[1:]:
        current_diff = calculate_pairwise_absolute_difference(X, Y)
        if current_diff < min_diff:
            min_diff = current_diff
            min_arr = Y
    return min_arr


def calculate_pairwise_absolute_difference(X, Y):
    n = min(len(X), len(Y))
    absolute_difference = 0
    for i in range(n):
        absolute_difference += abs(X[i] - Y[i])
    return absolute_difference


def test1():
    assert find_Y([1.3, 2.3, 4.4]) == (1, 2, 5)


if __name__ == "__main__":
    test1()
