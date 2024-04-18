# --------------------------
# Author: Tuan Nguyen
# Date created: 20200208
#!271.py
# --------------------------
"""
Given a sorted list of integers of length N, 
determine if an element x is in the list 
without performing any multiplication, division, or bit-shift operations.

Do this in O(log N) time.
"""


def exist(x, arr):
    """return True if x in sorted list arr"""
    if binary_search(x, arr, 0, len(arr) - 1) != -1:
        return True
    else:
        return False


def binary_search(x, arr, l, r):
    """return index of x in sorted list arr; -1 if x not in arr"""
    if l == r and x == arr[0]:  # sub-array has 1 element & it's x
        return l
    elif l == r and x != arr[0]:  # sub-array has 1 element, but it's not x
        return -1
    else:  # sub-array has > 1 element
        m = (l + r) // 2  # middle index
        if x == arr[m]:
            return m
        elif x < arr[m]:
            return binary_search(x, arr, l, m - 1)
        else:
            return binary_search(x, arr, m + 1, r)


# ----- UNIT TEST -----
def test1():
    assert exist(x=1, arr=[1, 3, 5, 7, 9]) == True


def test2():
    assert exist(x=2, arr=[1, 3, 5, 7, 9]) == False


if __name__ == "__main__":
    test1()
    test2()
