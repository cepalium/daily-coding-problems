# -----------------------------
# Author: Tuan Nguyen
# Date created: 20191025
#!165.py
# -----------------------------
"""
Given an array of integers, return a new array where each element in the new array 
is the number of smaller elements to the right of that element in the original input array.

For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0], since:

There is 1 smaller element to the right of 3
There is 1 smaller element to the right of 4
There are 2 smaller elements to the right of 9
There is 1 smaller element to the right of 6
There are no smaller elements to the right of 1
"""


def smaller_elements_to_right(arr):
    """return a new array where each element in the new array is the number of smaller elements
    to the right of that element in the original input array"""
    n = len(arr)
    smaller_elements = [0 for i in range(n)]
    for i in range(n):
        counter = 0
        for j in range(
            i + 1, n
        ):  # check all elements to the right of current marker
            if arr[i] > arr[j]:  # increment counter if find 1 smaller element
                counter += 1
        smaller_elements[i] = counter
    return smaller_elements


def test_smallerElements():
    assert smaller_elements_to_right([3, 4, 9, 6, 1]) == [1, 1, 2, 1, 0]


if __name__ == "__main__":
    test_smallerElements()
