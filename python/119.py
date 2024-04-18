# --------------------------
# Author: Tuan Nguyen
# Date created: 20191130
#!19.py
# --------------------------
"""
Given a set of closed intervals, find the smallest set of numbers that covers all the intervals. 
If there are multiple smallest sets, return any of them.

For example, given the intervals [0, 3], [2, 6], [3, 4], [6, 9], 
one set of numbers that covers all these intervals is {3, 6}.
"""

from operator import itemgetter


def smallest_cover_set(intervals):
    """return smallest set of numbers that covers all the intervals"""
    n = len(intervals)
    cover_set = set()
    # sort intervals ascendingly on end points
    sorted_intervals = sorted(intervals, key=itemgetter(1))
    bound = sorted_intervals[0][1]  # 1st bound: end point of 1st interval
    #
    i = 1  # index of currently-checked interval
    while i < n:  # go through all intervals
        if (
            bound >= sorted_intervals[i][0]
        ):  # current bound stabs the current interval
            i += 1
        else:  # current interval is out of current bound
            cover_set.add(bound)
            bound = sorted_intervals[i][
                1
            ]  # new bound is end point of current interval
    cover_set.add(bound)  # add last bound into set
    return cover_set


def test_smallest_cover_set():
    assert smallest_cover_set([[0, 3], [2, 6], [3, 4], [6, 9]]) == {3, 9}
    assert smallest_cover_set([(1, 4), (4, 5), (7, 9), (9, 12)]) == {4, 9}


if __name__ == "__main__":
    test_smallest_cover_set()
