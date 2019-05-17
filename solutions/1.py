# --------------------------
# Author: Tuan Nguyen
# Date: 20190514
# Task: Given a list of numbers and a number k, 
# return whether any two numbers from the list add up to k.
# --------------------------

def checkSum(arr: [], k):
# input: array of numbers & int k
# output: true/false if any 2 numbers in list add up to k
    for i in range(len(arr)-1):             # iterate from a[0] to a[len(a)-1]
        for j in range(i+1, len(arr), 1):   # iterate from a[i+1] to a[-1]
            if k == arr[i] + arr[j]:        # check sum
                return True
    return False


def unitTest(arr: [], k):
    print(arr, k, checkSum(arr, k))


if __name__ == "__main__":
    unitTest([10,5,2,7], 17)
    unitTest([10,5,2,7], 12)
    unitTest([10,5,2,7], 0)
    unitTest([10,5,2,7], -5)