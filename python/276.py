# --------------------------
# Author: Tuan Nguyen
# Date created: 20200213
#!276.py
# --------------------------
"""
Implement an efficient string matching algorithm.

That is, given a string of length N and a pattern of length k, 
write a program that searches for the pattern in the string with less than O(N * k) worst-case time complexity.

If the pattern is found, return the start index of its location. If not, return False.
"""


def pattern_matching(str, pat):
    """return start index of matching pattern in string"""
    N = len(str)
    k = len(pat)
    i = 0  # cursor
    if k == 0 or N == 0:  # trivial cases
        return False
    if k > N:
        return False
    while i < N - k:
        if str[i] == pat[0]:  # match first letter
            for j in range(k - 1, 0, -1):  # reversedly check matching letter
                if str[i + j] != pat[j]:  # unmatch found
                    i += k
                    break
                if j == 1 and str[i + j] == pat[j]:  # match pattern
                    return i
        i += 1
    return False


def test1():
    assert pattern_matching("abcdef", "cd") == 2


def test2():
    assert pattern_matching("Hard", "Work") == False


def test3():
    assert pattern_matching("abc", "") == False


def test4():
    assert pattern_matching("", "abc") == False


def test5():
    assert pattern_matching("qwerty", "qwew") == False


if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()
