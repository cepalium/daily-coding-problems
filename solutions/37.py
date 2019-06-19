# ------------------------------------------------
# Author: Tuan Nguyen
# Date: 20190619
#!solutions/37.py
# -----------------------------------------------
"""
The power set of a set is the set of all its subsets. 
Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, 
it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set.
"""

def convertIntToFixedLengthBinary(n, l):
# input: int n & length l
# output: binary string of n w/ length l
    bin_n = "{0:b}".format(n)   # convert int to binary
    if len(bin_n) < l:          # add "0" to front to have fixed length
        bin_n = "0"*(l - len(bin_n)) + bin_n
    return bin_n


def superSet(arr):
# input: array arr of ints
# output: superset from arr
    superSet = []
    len_arr = len(arr)
    for i in range(2**len_arr): # number of subsets = 2^len(array), e.g array has 3 elements -> superset has 8=2^3 subsets 
        bin_i = convertIntToFixedLengthBinary(i, len_arr)
        s = [arr[i] for i in range(len_arr) if bin_i[i] == "1"] # subset has all elements where "1" in bin_i 
        superSet.append(s)  # add subset into superset
    return superSet


def superSet_test(arr):
    print(arr, "-> ", superSet(arr))


if __name__ == "__main__":
    superSet_test([1, 2, 3])  # return [[]], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]