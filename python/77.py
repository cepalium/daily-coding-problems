# -------------------------------
# Author: Tuan Nguyen
# Date: 20190729
#!solutions/77.py
# -------------------------------
"""
Given a list of possibly overlapping intervals, 
return a new list of intervals where all overlapping intervals have been merged.

The input list is not necessarily ordered in any way.

For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], 
you should return [(1, 3), (4, 10), (20, 25)].
"""

def is_overlapped(a, b):
# input: 2 interval tuples a & b, format: (start, end)
# output: True/False if b is in a
    start_a, end_a = a[0], a[1]
    start_b, end_b = b[0], b[1]
    if start_a <= start_b <= end_b <= end_a:
        return True
    return False


def mergeOverlappingIntervals(intervals):
# input: list of tuples 'intervals', each tuple has format (start, end)
# output: list after merging all overlapping intervals
# running time: O(n^2)
    # trivial
    if len(intervals) < 2:
        return intervals
    # else: have intervals
    mergedIntervals = []    # init output
    # add 1st interval into output
    mergedIntervals.append(intervals[0])
    for i in intervals[1:]:
        new_flag = True # flag to check if the currently-checked interval is in the output list
        pivot = 0
        while pivot < len(mergedIntervals):
            merged_i = mergedIntervals[pivot]
            if new_flag and is_overlapped(i, merged_i):  # the currently-checked interval includes the already checked interval
                mergedIntervals[pivot] = i  # replace with the currently-checked interval
                new_flag = False
                pivot += 1
                continue
            if new_flag and is_overlapped(merged_i, i): # the already-checked interval includes the currently-checked interval
                new_flag = False
                pivot += 1
                continue
            if (not new_flag) and is_overlapped(i, merged_i):   # the currently-checked interval is already added to output list & includes the already-checked interval
                mergedIntervals.remove(merged_i)
                continue
            if (not new_flag) and is_overlapped(merged_i, i):   # the currently-checked interval is already added to output list & is included by an already-checked interval
                mergedIntervals.remove(i)
                continue
            pivot += 1
        if new_flag:    # the currently-checked interval is totally different to all intervals in output list
            mergedIntervals.append(i)
            
    return mergedIntervals


def mergeOverlappingIntervals_test(intervals):
    print(intervals, '~>', mergeOverlappingIntervals(intervals))


if __name__ == "__main__":
    mergeOverlappingIntervals_test([(1, 3), (5, 8), (4, 10), (20, 25)]) # return [(1, 3), (4, 10), (20, 25)]
    mergeOverlappingIntervals_test([(1, 3), (5, 8), (20, 25)]) # return [(1, 3), (5, 8), (20, 25)]
    mergeOverlappingIntervals_test([(1, 3), (5, 8), (1, 10)]) # return [(1, 10)]