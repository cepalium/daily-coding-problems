# --------------------------------
# Author: Tuan Nguyen
# Date created: 20190930
#!solutions/140.py
# --------------------------------
"""
Given an array of integers in which two elements appear exactly once and all other elements appear exactly twice, 
find the two elements that appear only once.

For example, given the array [2, 4, 6, 8, 10, 2, 6, 10], return 4 and 8. 
The order does not matter.

Follow-up: Can you do this in linear time and constant space?
"""

def findUniqueElements1(array):
# input: array of integers s.t 2 elements appear exactly once and all other elements appear exactly twice
# output: array of 2 elements that appear only once
# method: pythonic method of list
# running time: O(n^2); space complexity: O(1)
    return [x for x in array if array.count(x) == 1]


def findUniqueElements2(array):
# input: array of integers s.t 2 elements appear exactly once and all other elements appear exactly twice
# output: array of 2 elements that appear only once
# method: sort array, then eliminate duplicate
# running time: O(n*log n); space complexity: O(1)
    n = len(array)
    array = sorted(array)     # in-place sorting takes O(n*log n)
    output = []
    j = 0
    while j < n-1:
        if array[j] == array[j+1]:
            j += 2      # find duplicates ~> jump 2 index
        else:
            output.append(array[j])   # find the appear-once element
            j += 1                          # increment index by 1
    return output


def findUniqueElements3(array):
# input: array of integers s.t 2 elements appear exactly once and all other elements appear exactly twice
# output: array of 2 elements that appear only once
# method: dict to store frequency of elements; if frequency == 2, delete pair from dict
# running time: O(n); space complexity: O(n)
    freq = {x:0 for x in array}     # frequency dictionary initialized ~> O(n)
    output = []                     # output list initialized
    for x in array:
        freq[x] += 1                # count frequency of each elements by increment ~> O(n)
    for k, v in freq.items():
        if v == 1:
            output.append(k)        # add elements of 1 occurence to output
    return output


def findUniqueElements_test(array, desiredVal):
    print(findUniqueElements1(array) == desiredVal, 
            findUniqueElements2(array) == desiredVal, 
            findUniqueElements3(array) == desiredVal)


if __name__ == "__main__":
    findUniqueElements_test([2, 4, 6, 8, 10, 2, 6, 10], [4, 8])