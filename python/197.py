# -------------------------
# Author: Tuan Nguyen
# Date created: 20191126
#!197.py
# -------------------------
"""
Given an array and a number k that's smaller than the length of the array, 
rotate the array to the right k elements in-place.
"""

def rotate(arr, k):
    """ rotate arr to the right k elements in-place """
    n = len(arr)
    for _ in range(k):
        temp = arr[n-1]
        for i in range(n-1, 0, -1):
            arr[i] = arr[i-1]   # shift right 1 position
        arr[0] = temp           # last elemenet becomes first

def test_rotate1():
    arr = [1,2,3,4,5]
    rotate(arr, 1)
    assert arr == [5,1,2,3,4]

def test_rotate2():
    arr = [1,2,3,4,5]
    rotate(arr, 2)
    assert arr == [4,5,1,2,3]

def test_rotate3():
    arr = [1,2,3,4,5]
    rotate(arr, 3)
    assert arr == [3,4,5,1,2]
    
def test_rotate4():
    arr = [1,2,3,4,5]
    rotate(arr, 4)
    assert arr == [2,3,4,5,1]

if __name__ == "__main__":
    test_rotate1()
    test_rotate2()
    test_rotate3()
    test_rotate4()