# --------------------------------
# Author: Tuan Nguyen
# Date created: 20190515
#
# Task:
# Given an array of integers, 
# return a new array such that each element at index i of the new array 
# is the product of all the numbers in the original array except the one at i.
# ----------------------------------

def productList(arr: []):
# input: an array of integers
# output: new array s.t a[i] = product(li[::]) / li[i]
    prodArr = []       # init output array
    totalProd = 1       # init var of total product of all elements in input list
    for e in arr:       # calculate the total product
        totalProd *= e
    
    for i in range(len(arr)):   # add element of new array, i.e a[i] = totalProd / li[i]
        prodArr.append(totalProd/arr[i])
    
    return prodArr


def unitTest(arr: []):
    print(arr, productList(arr))


if __name__ == "__main__":
    unitTest([1,2,3,4,5])
    unitTest([3,2,1])