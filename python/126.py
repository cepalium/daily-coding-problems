# ----------------------
# Author: Tuan Nguyen
# Date created: 20190916
#!solutions/126.py
# ----------------------
"""
Write a function that rotates a list by k elements. 
For example, [1, 2, 3, 4, 5, 6] rotated by two becomes [3, 4, 5, 6, 1, 2]. 
Try solving this without creating a copy of the list. 
How many swap or move operations do you need?
"""


def pythonicRotate(l, k):
    # input: list l & int k
    # output: returns a list after k rotation
    # method: concat list
    return l[k:] + l[:k]


def rorate(l, k):
    # input: list l & int k
    # output: returns a list after k rotation
    # method: swap elements for each rotation
    # need [len(l) - 1] * k swap operation ~> O(n*k) swap operations, with n = len(l)
    for _ in range(k):
        for j in range(len(l) - 1):
            l[j], l[j + 1] = l[j + 1], l[j]
    return l


def rotate_test(l, k):
    print(
        "l={}, k={} ~> {} | {}".format(
            l, k, pythonicRotate(l, k), rorate(l, k)
        )
    )


if __name__ == "__main__":
    rotate_test([1, 2, 3, 4, 5, 6], 2)  # print [3, 4, 5, 6, 1, 2]
    rotate_test([1, 2, 3, 4, 5, 6, 7], 3)  # print [3, 4, 5, 6, 1, 2]
    rotate_test([], 3)  # print []
    rotate_test([1], 2)  # print [1]
