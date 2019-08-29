# -------------------------
# Author: Tuan Nguyen
# Date create: 20190829
#!solutions/108.py
# -------------------------
"""
Given two strings A and B, 
return whether or not A can be shifted some number of times to get B.

For example, if A is abcde and B is cdeab, return true. 
If A is abc and B is acb, return false.
"""

def isShifted(A, B):
# input: 2 strings A & B
# output: returns true if A can be shifted to get B, otherwise false
    if len(A) != len(B):    # 2 strings have different length
        return False
    for j in range(len(A)): # each iteration shift A 1 position to left
        if A[j] == B[0]:    # only continue when 1st char in shifted A matches 1st char in B
            shiftedA = A[j:] + A[:j]    # construct full shifted A
            if shiftedA == B:   
                return True # shifted A matches B
    return False    # reach this ~> no possible shift


def isShifted_test(A, B):
    print("A={}, B={} ~> is shifted: {}".format(A, B, isShifted(A, B)))


if __name__ == "__main__":
    isShifted_test(A="abcde", B="cdeab")    # return True
    isShifted_test(A="abc", B="acb")    # return False