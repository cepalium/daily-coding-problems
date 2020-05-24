# ----------------------------------
# Author: Tuan Nguyen
# Date created: 20200524
#!377.py
# ----------------------------------
"""
Given an array of numbers arr and a window of size k, 
print out the median of each window of size k starting 
from the left and moving right by one position each time.

For example, given the following array and k = 3:

[-1, 5, 13, 8, 2, 3, 3, 1]

Your function should print out the following:

5 <- median of [-1, 5, 13]
8 <- median of [5, 13, 8]
8 <- median of [13, 8, 2]
3 <- median of [8, 2, 3]
3 <- median of [2, 3, 3]
3 <- median of [3, 3, 1]

Recall that the median of an even-sized list 
is the average of the two middle numbers.
"""
def print_median_each_window(arr, k):
    n = len(arr)
    for i in range(n-k+1):
        print_median(arr[i:i+k])

def print_median(arr):
    m = median(arr)
    print("{} <- median of {}".format(m, arr))

def median(arr):
    n = len(arr)
    arr = sorted(arr)
    if n % 2 == 0:  # even-sized array
        return (arr[n//2 - 1] + arr[n//2]) / 2  # median = average of 2 middle numbers
    return arr[n//2]


def test1():
    print_median_each_window([-1, 5, 13, 8, 2, 3, 3, 1], 3)

def test2():
    print_median_each_window([-1, 5, 13, 8, 2, 3, 3, 1], 4)

def test3():
    print_median_each_window([-1, 5, 13, 8, 2, 3, 3, 1], 5)

if __name__ == "__main__":
    test1()
    test2()
    test3()