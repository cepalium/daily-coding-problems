# ----------------------------
# Author: Tuan Nguyen
# Date created: 20191003
#!solutions/143.py
# ----------------------------
"""
Given a pivot x, and a list lst, partition the list into three parts.

The first part contains all elements in lst that are less than x
The second part contains all elements in lst that are equal to x
The third part contains all elements in lst that are larger than x 
Ordering within a part can be arbitrary.

For example, given x = 10 and lst = [9, 12, 3, 5, 14, 10, 10], 
one partition may be [9, 3, 5, 10, 10, 12, 14]
"""

def partition(lst, x):
# input: list lst of integers & pivot int x
# output: list s.t partition into 3 parts: less than x, equal to x, larger than x
# running time: O(n)
    L = []  # list L of elements less than x initialized
    E =[]   # list E of elements equal to x initialized
    G = []  # list G of elements larger than x initialized
    # partition input list into 3 sub-lists L, E, G
    for e in lst:
        if e < x:
            L.append(e)
        elif e == x:
            E.append(e)
        else:
            G.append(e)
    return L + E + G


def partition_test(lst, x, desiredVal):
    print(partition(lst, x) == desiredVal)


if __name__ == "__main__":
    partition_test(lst=[9, 12, 3, 5, 14, 10, 10], x=10, desiredVal=[9, 3, 5, 10, 10, 12, 14])
