# ----------------------------
# Author: Tuan Nguyen
# Date created: 20200125
#!257.py
# ----------------------------
"""
Given an array of integers out of order, determine the bounds of the smallest window that must be sorted in order for the entire array to be sorted. 
For example, given [3, 7, 5, 6, 9], you should return (1, 3).
"""
def min_bound(arr):
    """ return the bound of smallest window to sort the input array """
    n = len(arr)
    min_num, min_num_idx = arr[0], 0
    start = end = 0
    marker = 1          # running index
    bounds = []         # store all bounds of sorting window
    while marker < n:
        if arr[marker] <= arr[start] and arr[marker] > min_num:
            end += 1
        elif arr[marker] <= arr[start] and arr[marker] < min_num:
            end += 1
            if min_num_idx < start:             # min element is outside current window (start, end)
                start = min_num_idx
                min_num, min_num_idx = arr[marker], marker
        else:                                   # arr[marker] > arr[start]
            if start != end:
                bounds.append((start, end))
            start = end = marker                # restart new window
        marker += 1
    if start != end:                            # special: add bound for descending array b/c 'else' in while-loop could not cover this case
        bounds.append((start, end))
    if bounds:
        return bounds[-1]
    else:               # no bound found
        return 0

def test_min_bound():
    assert min_bound([3, 7, 5, 6, 9]) == (1, 3)
    assert min_bound([1, 2, 3, 4, 5]) == 0
    assert min_bound([5, 4, 3, 2, 1]) == (0, 4)
    assert min_bound([3, 7, 5, 6, 9, 2]) == (0, 5)
    assert min_bound([3, 7, 5, 6, 9, 2, 1]) == (0, 6)

if __name__ == "__main__":
    test_min_bound()