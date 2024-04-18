# ----------------------------
# Author: Tuan Nguyen
# Date created: 20190911
#!solutions/40.py
# ----------------------------
"""
Given an array of integers where every integer occurs three times except for one integer, which only occurs once, 
find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.
"""


def findNonduplicatedInteger(array):
    # input: array of integers s.t every integer occurs 3 times except for 1 integer, which occurs once
    # output: return the non-duplicated integer
    # running time: O(n)
    # space complexity: O(1)
    freq = {}  # {int: frequency}
    # go through all elements in array
    for a in array:
        if a not in freq.keys():  # create key in dict if 1st time
            freq[a] = 1
        else:
            freq[a] += 1  # increase frequency of this key
            if freq[a] == 3:  # if this key appears 3 times
                del freq[a]  # then delete it from dict
    return list(freq.keys())[
        0
    ]  # return the only 1 key in dict, i.e non-duplicated integer


def findNonduplicatedInteger_test(array):
    print(array, "~>", findNonduplicatedInteger(array))


if __name__ == "__main__":
    findNonduplicatedInteger_test([6, 1, 3, 3, 3, 6, 6])  # return 1
    findNonduplicatedInteger_test([13, 19, 13, 13])  # return 19
