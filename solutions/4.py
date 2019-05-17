# --------------------------
# Author: Tuan Nguyen
# Date: 20190517
# Task: Given an array of integers, 
# find the first missing positive integer in linear time and constant space. 
# i.e find the lowest positive integer that does not exist in the array. 
# The array can contain duplicates and negative numbers as well.
# --------------------------

def missingLowestPositiveInteger(arr: []):
# input: array of int 'arr'
# output: the lowest positive int that does not exist in input array
    missingLPInt = 0    # init the var of missing Lowest Positive Int
    posArr = [n for n in arr if n > 0]  # new array of only positive ints from input array
    
    for i in range(len(posArr)):
        # initial case
        if ((i==0) and (posArr[i] != 1)):
            missingLPInt = 1
        if ((i==0) and (posArr[i] == 1)):
            missingLPInt = 2
        # find missingLPInt
        if (posArr[i] == missingLPInt):
            missingLPInt += 1
            while missingLPInt in posArr:
                missingLPInt += 1       # increase by 1 until the missingLPInt not in posArr, i.e the true missingLPInt up to index i

    return missingLPInt


def unitTest(arr: []):
    print(arr, missingLowestPositiveInteger(arr))


if __name__ == "__main__":
    unitTest([3,4,-1,1])
    unitTest([1,2,0])
    unitTest([3,4,-1,1,2])
    unitTest([3,5,-1,1,2])
