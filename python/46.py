# --------------------------------
# Author: Tuan Nguyen
# Date: 20190628
#!solutions/46.py
# --------------------------------
"""
Given a string, find the longest palindromic contiguous substring. 
If there are more than one with the maximum length, return any one.

For example, the longest palindromic substring of "aabcdcb" is "bcdcb". 
The longest palindromic substring of "bananas" is "anana".
"""

def is_palindromic(string):
# input: a string 'string'
# output: True/False if 'string' is palindromic
    for i in range(int(len(string)/2)):
        if string[i] != string[-1-i]:
            return False
    return True


def longestPalindromicSubstring_pivotToRight(string):
# input: a string 'string'
# output: longest palindromic substring of 'string' w/ following method:
# method: if left pivots != right pivots, left pivots move right
# ~> this method misses the palindromic substring which starts from left pivots to before right pivots
# ~> suggest applying this method again with inversed string to get the correct answer
# running time: O(n)
    forwardLongestPalindromicSubstring = ''
    # init pivots
    lo = 0  # init outer left pivot
    li = lo + 1 # init inner left pivot
    ro = len(string) - 1    # init outer right pivot
    ri = ro - 1 # init inner right pivot
    while li <= ro:
        # print(lo, li, ri, ro, string[lo], string[li], string[ri], string[ro])
        if ri <= li <= ri + 1 and is_palindromic(string[lo:ro+1]):
            forwardLongestPalindromicSubstring = string[lo:ro+1]
            break
        if (string[lo] == string[ro]) and (string[li] == string[ri]):
            li += 1
            ri -= 1
            continue
        elif string[lo] == string[ri]:
            ro = ri
            ri -= 1
        elif string[li] == string[ro]:
            lo = li
            li += 1
        elif (string[lo] != string[ro]) and (string[li] == string[ri]):
            lo = li
            li += 1
            ro = ri
            ri -= 1
        else:   # left pivots move right
            lo += 1
            li = lo + 1
    return forwardLongestPalindromicSubstring


def longestPalindromicSubstring(string):
# input: a string 'string'
# output: longest palindromic substring of 'string' 
# running time: O(n)
    longestPalindromicSubstring = ''
    leftToRight_longestPalindromicSubstring = longestPalindromicSubstring_pivotToRight(string)
    rightToLeft_longestPalindromicSubstring = longestPalindromicSubstring_pivotToRight(string[::-1])    # input inversed string for method
    if len(leftToRight_longestPalindromicSubstring) > len(rightToLeft_longestPalindromicSubstring):
        longestPalindromicSubstring = leftToRight_longestPalindromicSubstring
    else:
        longestPalindromicSubstring = rightToLeft_longestPalindromicSubstring[::-1]
    return longestPalindromicSubstring


def longestPalindromicSubstring_test(string):
    print(string, '~> longest palindromic substring:', longestPalindromicSubstring(string))


if __name__ == "__main__":
    longestPalindromicSubstring_test("aabcdcb") # print 'bcdcb'
    longestPalindromicSubstring_test("bananas") # print 'anana'
    longestPalindromicSubstring_test("abceba") # print ''
    longestPalindromicSubstring_test("abeeba") # print 'abeeba'
    longestPalindromicSubstring_test("abcecba") # print 'abcecba'
    longestPalindromicSubstring_test("bcdcbaa") # print 'bcdcb'
    longestPalindromicSubstring_test("abcdef")  # print ''

