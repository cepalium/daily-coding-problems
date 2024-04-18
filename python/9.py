# ----------------------
# Author: Tuan Nguyen
# Date: 20190522
# ----------------------
"""
Problem:

Given a list of integers, 
write a function that returns the largest sum of non-adjacent numbers. 
Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. 
[5, 1, 1, 5] should return 10, since we pick 5 and 5.
"""


def nonadjacentLargestSum(l):
    # input: list of ints
    # output: largest sum of non-adjacent numbers
    # method: dynamic programming
    if len(l) < 3:  # list of up to 2 elements
        return max(l)
    else:
        s = [l[0], l[1]]
        for i in range(2, len(l)):
            s.append(l[i] + max(s[:-1]))  # s[i] = l[i] + max{ s[j] | j<i-1 }
    return max(s)


def nonadjacentLargestSum_test(li):
    print(li, nonadjacentLargestSum(li))


if __name__ == "__main__":
    nonadjacentLargestSum_test([2, 4, 6, 2, 5])  # return 13
    nonadjacentLargestSum_test([5, 1, 1, 5])  # return 10
    nonadjacentLargestSum_test([10])  # return 10
    nonadjacentLargestSum_test([1, 3])  # return 3
    nonadjacentLargestSum_test([1, 3, 2])  # return 3
