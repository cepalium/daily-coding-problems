# --------------------------
# Author: Tuan Nguyen
# Date created: 20191017
#!solutions/156.py
# --------------------------
"""
Given a positive integer n, find the smallest number of squared integers which sum to n.

For example, given n = 13, return 2 since 13 = 32 + 22 = 9 + 4.

Given n = 27, return 3 since 27 = 32 + 32 + 32 = 9 + 9 + 9.
"""

def smallest_number_squared_integers(n):
    """ return smallest number of squared integers which sum to n 
    * ensure to have result because having 1 as smallest unit & n is positive int """
    squared_integer_list = [i**2 for i in range(n//2, 0, -1) if i**2 <= n]  # list of squared integers up to n descendingly
    m = len(squared_integer_list)
    smallest = None     # output smallest number initialized
    for j in range(m):  # each iteration drops a number in squared_integer_list
        number = possible_smallest(n, squared_integer_list, j)  # find the number of integers which sum to n
        if (smallest is None) or (number < smallest):           # update smallest number if possible
            smallest = number
    return smallest
            

def possible_smallest(n, lst, marker):
    """ recursively find the number of integers from lst which sum to n """
    if n == 0:
        return 0
    else:
        q = n // lst[marker]
        r = n % lst[marker]
        return q + possible_smallest(r, lst, marker+1)


def smallestNumberSquaredIntegers_test(n, desiredVal):
    assert smallest_number_squared_integers(n) == desiredVal


if __name__ == "__main__":
    smallestNumberSquaredIntegers_test(n=13, desiredVal=2)
    smallestNumberSquaredIntegers_test(n=27, desiredVal=3)