# ----------------------------------
# Author: Tuan Nguyen
# Date created: 20200521
#!374.py
# ----------------------------------
"""
Given a sorted array arr of distinct integers, 
return the lowest index i for which arr[i] == i. 
Return null if there is no such index.

For example, given the array [-5, -3, 2, 3], 
return 2 since arr[2] == 2. Even though arr[3] == 3, 
we return 2 since it's the lowest index.
"""
def lowest_matching_index(arr):
    for i, arr_i in enumerate(arr):
        if i == arr_i:
            return i
    return None


def test1():
    assert lowest_matching_index([-5, -3, 2, 3]) == 2

def test2():
    assert lowest_matching_index([1, 2, 3, 4, 5]) == None

def test3():
    assert lowest_matching_index([0, 1, 2, 3, 4]) == 0

if __name__ == "__main__":
    test1()
    test2()
    test3()