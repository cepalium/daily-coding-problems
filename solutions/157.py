# --------------------------
# Author: Tuan Nguyen
# Date created: 20191017
#!solutions/157.py
# --------------------------
"""
Given a string, determine whether any permutation of it is a palindrome.

For example, carrace should return true, since it can be rearranged to form racecar, which is a palindrome. 
daily should return false, since there's no rearrangement that can form a palindrome.
"""

from itertools import permutations

def is_permutation_palindrome(str):
    """ return True if any permutation of string str is a palindrome """
    for s in permutations(str): # loop through all permutations of str
        if is_palindrome(s):
            return True # successfully find a palindrome permutation
    return False        # reach this, then no possible permutation is palindrome


def is_palindrome(str):
    """ return True if string str is palindrome """
    n = len(str)
    for i in range(n//2):       # loop to middle of string str
        if str[i] != str[-1-i]:
            return False    # find a character doesn't match with its mirror-positioned character
    return True     # reach this, then str is palindrome


def palindromePermutation_test(str, desiredVal):
    assert is_permutation_palindrome(str) == desiredVal


if __name__ == "__main__":
    palindromePermutation_test(str="carrace", desiredVal=True)
    palindromePermutation_test(str="daily", desiredVal=False)