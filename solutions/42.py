# ---------------------------------
# Author: Tuan Nguyen
# Date: 20190624
#!solutions/42.py
# ---------------------------------
"""
Given a list of integers S and a target number k,
write a function that returns a subset of S that adds up to k. 
If such a subset cannot be made, then return null.

Integers can appear more than once in the list. 
You may assume all numbers in the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, 
return [12, 9, 2, 1] since it sums up to 24.
"""

def convertIntToFixedLengthBinary(n, l):
# input: int 'n' & length 'l'
# output: binary string of n of size l
    bin_n = "{0:b}".format(n)
    if len(bin_n) < l:
        bin_n = '0'*(l - len(bin_n)) + bin_n
    return bin_n


def subSetToSum(S, k):
# intput: list 'S' of integers & target int 'k'
# output: return subset of 'S' that adds up to k
# method: find superset add to k
    lenS = len(S)
    for i in range(2**lenS):
        bin_i = convertIntToFixedLengthBinary(i, lenS)
        s = [S[j] for j in range(lenS) if bin_i[j] == '1']  # create subset of S
        if sum(s) == k:
            return s
    return []


def subSetToSum_test(S, k):
    print(S, '-> ', k, ' -> ', subSetToSum(S, k))


if __name__ == "__main__":
    subSetToSum_test(S=[12, 1, 61, 5, 9, 2], k=24)  # return [12, 9, 2, 1]
    subSetToSum_test(S=[12, 1, 61, 5, 9, 2], k=0)  # return []
    subSetToSum_test(S=[12, 1, 61, 5, 9, 2], k=61)  # return [61]