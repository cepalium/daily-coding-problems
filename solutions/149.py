# --------------------------
# Author: Tuan Nguyen
# Date created: 20191010
#!solutions/149.py
# --------------------------
"""
Given a list of numbers L, implement a method sum(i, j) which returns the sum from the sublist L[i:j] (including i, excluding j).

For example, given L = [1, 2, 3, 4, 5], sum(1, 3) should return sum([2, 3]), which is 5.

You can assume that you can do some pre-processing. sum() should be optimized over the pre-processing step.
""" 

class IntegerList:
    """ constructor """
    def __init__(self, lst):
        # create a list of prefix sum from lst
        total = 0
        self.prefixSum = []
        for e in lst:
            total += e
            self.prefixSum.append(total)
    
    """ returns the sum from the sublist L[i:j] (including i, excluding j) """
    def sum(self, i, j):
        if i < 0 or j >= len(self.prefixSum):   # validate
            raise IndexError("Invalid index")
        if i >= j:
            return 0
        elif i == 0:
            return self.prefixSum[j-1]    # sum from sublist[0:j]
        else:                       
            return self.prefixSum[j-1] - self.prefixSum[i-1]    # sum from sublist [i:j]


def test(arr, i, j, desiredVal):
    L = IntegerList(arr)
    print(L.sum(i, j) == desiredVal)


if __name__ == "__main__":
    test(arr=[1,2,3,4,5], i=1, j=3, desiredVal=5)
    test(arr=[1,2,3,4,5], i=0, j=3, desiredVal=6)
    test(arr=[1,2,3,4,5], i=1, j=1, desiredVal=0)
    test(arr=[1,2,3,4,5], i=0, j=4, desiredVal=10)