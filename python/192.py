# --------------------------
# Author: Tuan Nguyen
# Date created: 20191121
#!192.py
# --------------------------
"""
You are given an array of nonnegative integers. 
Let's say you start at the beginning of the array and are trying to advance to the end. 
You can advance at most, the number of steps that you're currently on. 
Determine whether you can get to the end of the array.

For example, given the array [1, 3, 1, 2, 0, 1], 
we can go from indices 0 -> 1 -> 3 -> 5, so return true.

Given the array [1, 2, 1, 0, 0], we can't reach the end, so return false.
"""


def hopping_reach_end(arr, start):
    """return True if the end of array could be reach from a start index"""
    n = len(arr)
    reachable = [
        False for i in range(n)
    ]  # boolean array of reachable: False = unreachable, True = reachable
    reachable[start] = True  # base case
    for i in range(start, n):  # dynamic programming
        max_hop = arr[i]
        if reachable[i] is True and max_hop > 0:
            for j in range(1, max_hop + 1):
                if i + j < n:
                    reachable[i + j] = True
    return reachable[n - 1]  # True if last element is reachable


def test_hopping():
    assert hopping_reach_end([1, 3, 1, 2, 0, 1], 0) == True
    assert hopping_reach_end([1, 2, 1, 0, 0], 0) == False


if __name__ == "__main__":
    test_hopping()
