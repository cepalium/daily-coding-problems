# ------------------------
# Author: Tuan Nguyen
# Date created: 20191118
#!189.py
# ------------------------
"""
Given an array of elements, 
return the length of the longest subarray where all its elements are distinct.

For example, given the array [5, 1, 3, 5, 2, 3, 4, 1], 
return 5 as the longest subarray of distinct elements is [5, 2, 3, 4, 1].
"""

def length_distinct_longest_subarray(arr):
    """ return the length of the longest subarray where all its elements are distinct """
    queue = []  # current longest sequence of distinct elements
    max = -1    # max length
    for i in arr:
        while i in queue:   # element i is duplicated
            queue.pop(0)    # pop 1st element until no duplicate
        queue.append(i)
        max = len(queue) if len(queue) > max else max   # update max length if possible
    return max

def test_length():
    assert length_distinct_longest_subarray([5, 1, 3, 5, 2, 3, 4, 1]) == 5
    assert length_distinct_longest_subarray([5, 3, 2, 3, 4, 1]) == 4

if __name__ == "__main__":
    test_length()