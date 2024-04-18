# --------------------------
# Author: Tuan Nguyen
# Date created: 20190918
#!solutions/111.py
# --------------------------
"""
Given a word W and a string S, find all starting indices in S which are anagrams of W.

For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4.
"""


def indicesStartingAnagram(S, W):
    # input:  string S & word W
    # output: list of all starting indices in S which are anagrams of W
    # running time: O(n*m*log m) where n=len(S) & m=len(W)
    # instance variables
    n_s = len(S)
    n_w = len(W)
    # output list initialized
    l = []
    for j in range(0, n_s - n_w + 1):
        if isAnagram(S[j : j + n_w], W):
            l.append(j)
    return l


def isAnagram(s1, s2):
    # input: 2 string s1 & s2
    # output: returns boolean True if s1 is anagram of s2; otherwise False
    # running: O(m*log m), where m=len(string)
    if len(s1) != len(s2):
        return False
    # create 2 sorted lists of characters from 2 input strings
    c1 = sorted(list(s1))
    c2 = sorted(list(s2))
    if c1 != c2:  # 2 lists are not equal
        return False
    return True


def indicesStartingAnagram_test(S, W, desiredVal):
    print(
        "S={}, W={}\nDesired val= {}, assert={}".format(
            S, W, desiredVal, indicesStartingAnagram(S, W) == desiredVal
        )
    )


if __name__ == "__main__":
    indicesStartingAnagram_test(
        S="abxaba", W="ab", desiredVal=[0, 3, 4]
    )  # print True
