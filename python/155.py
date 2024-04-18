# ----------------------------
# Author: Tuan Nguyen
# Date created: 20191015
#!solutions/155.py
# -----------------------------
"""
Given a list of elements, find the majority element, 
which appears more than half the time (> floor(len(lst) / 2.0)).

You can assume that such element exists.

For example, given [1, 2, 1, 1, 3, 4, 0], return 1.
"""


def majorityElement(lst):
    """return the majority element from lst, which appears > half the time"""
    freq = (
        {}
    )  # dictionairy initialized: {element in list : its frequency in list}
    majE = None  # output initialized
    # count frequencies of each distinct elements in lst
    for e in lst:
        if e not in freq.keys():
            freq[e] = 1
        else:
            freq[e] += 1
    # find majority element
    for k, v in freq.items():
        if v >= (len(lst) // 2):
            majE = k
    return majE


def majorityElement_test(lst, desiredVal):
    print(majorityElement(lst) == desiredVal)


if __name__ == "__main__":
    majorityElement_test(lst=[1, 2, 1, 1, 3, 4, 0], desiredVal=1)
    majorityElement_test(lst=[], desiredVal=None)
    majorityElement_test(lst=[1, 2, 2], desiredVal=2)
    majorityElement_test(lst=[1, 2, 2, 3, 3, 3], desiredVal=3)
