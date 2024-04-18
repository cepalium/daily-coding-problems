# -----------------------------------
# Author: Tuan Nguyen
# Date: 20190617
#!solutions/35.py
# -----------------------------------
"""
Given an array of strictly the characters 'R', 'G', and 'B', 
segregate the values of the array 
so that all the Rs come first, the Gs come second, and the Bs come last. 
You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], 
it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
"""


def sortRGB(arr):
    # input: list arr of characters 'R', 'G', 'B'
    # output: sorted array which Rs first, Gs second, Bs last
    # push 'B' to back
    l = 0
    r = len(arr) - 1
    while l < r:
        if (arr[l] == "B") and (arr[r] != "B"):
            arr[l], arr[r] = arr[r], arr[l]  # swap 'B' to back
            l += 1
            r -= 1
        elif arr[r] == "B":
            r -= 1
        else:
            l += 1
    # push 'R' to front
    l = 0
    r = len(arr) - 1
    while l < r:
        if (arr[l] != "R") and (arr[r] == "R"):
            arr[l], arr[r] = arr[r], arr[l]  # swap 'R' to front
            l += 1
            r -= 1
        elif arr[l] == "R":
            l += 1
        else:
            r -= 1
    return arr


def sortRGB_test(array):
    print(array, "-> ", sortRGB(array))


if __name__ == "__main__":
    sortRGB_test(
        ["G", "B", "R", "R", "B", "R", "G"]
    )  # return ['R', 'R', 'R', 'G', 'G', 'B', 'B']
    sortRGB_test(
        ["B", "G", "R", "B", "G", "R", "B", "G", "R"]
    )  # return ['R', 'R', 'R', 'G', 'G', 'G', 'B', 'B', 'B']
    sortRGB_test(
        ["G", "B", "R", "R", "R", "R", "R"]
    )  # return ['R', 'R', 'R', 'R', 'R', 'G', 'B']
