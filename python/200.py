# --------------------------
# Author: Tuan Nguyen
# Date created: 20191130
#!200.py
# --------------------------
"""
Let X be a set of n intervals on the real line. 
We say that a set of points P "stabs" X if every interval in X contains at least one point in P. 
Compute the smallest set of points that stabs X.

For example, given the intervals [(1, 4), (4, 5), (7, 9), (9, 12)], you should return [4, 9].
"""

from operator import itemgetter

def smallest_stab_set(X):
    """ return the smallest set of points that stabs all intervals in X"""
    n = len(X)
    stab_set = set()                    # output
    # sort X ascendingly on end point of interval
    sorted_X = sorted(X, key=itemgetter(1))
    bound = sorted_X[0][1]              # 1st bound: end point of 1st interval
    # generate stab set
    i = 1           # index of currently-checked interval in sorted_X
    while i < n:    # go through all intervals
        if bound >= sorted_X[i][0]:     # bound stabs X
            i += 1                      # move to next interval
        else:
            stab_set.add(bound)         # add current bound to stab set
            bound = sorted_X[i][1]      # update bound = end point of current interval
    stab_set.add(bound)                 # add the last bound to stab set
    return stab_set


def test_smallest_stab_set():
    assert smallest_stab_set([[0, 3], [2, 6], [3, 4], [6, 9]]) == {3, 9}
    assert smallest_stab_set([(1, 4), (4, 5), (7, 9), (9, 12)]) == {4, 9}

if __name__ == "__main__":
    test_smallest_stab_set()