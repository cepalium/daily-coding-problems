# --------------------------------
# Author: Tuan Nguyen
# Date: 20190515
# ----------------------------------
"""
Problem:

Given an array of integers, 
return a new array such that each element at index i of the new array 
is the product of all the numbers in the original array except the one at i.

For example, 
* if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]
* if our input was [3, 2, 1], the expected output would be [2, 3, 6]

"""
from typing import List


def productList(arr: List[int]) -> List[int]:
    # input: an array of integers
    # output: new array s.t a[i] = product(li[::]) / li[i]
    prodArr = []  # init output array
    totalProd = 1  # init var of total product of all elements in input list
    for e in arr:  # calculate the total product
        totalProd *= e

    for i in range(
        len(arr)
    ):  # add element of new array, i.e a[i] = totalProd / li[i]
        prodArr.append(totalProd / arr[i])

    return prodArr


if __name__ == "__main__":
    assert productList(arr=[1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
    assert productList(arr=[3, 2, 1]) == [2, 3, 6]
