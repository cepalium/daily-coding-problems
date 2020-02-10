# ------------------------------
# Author: Tuan Nguyen
# Date created: 20200210
#!273.py
# ------------------------------
"""
A fixed point in an array is an element whose value is equal to its index. 
Given a sorted array of distinct elements, return a fixed point, if one exists. Otherwise, return False.

For example, given [-6, 0, 2, 40], you should return 2. 
Given [1, 5, 7, 8], you should return False.
"""
def fixed_point(arr):
    """ return a fixed point in sorted array if exist; else False """
    for i, a_i in enumerate(arr):
        if i == a_i:
            return a_i
        elif i < a_i:    # all next elements in array will be bigger than their indices
            return False
        else:
            continue
    return False

def test1():
    assert fixed_point([-6, 0, 2, 40]) == 2

def test2():
    assert fixed_point([1, 5, 7, 8]) == False

if __name__ == "__main__":
    test1()
    test2()