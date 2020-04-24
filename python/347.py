# --------------------------
# Author: Tuan Nguyen
# Date created: 20200424
#!347.py
# --------------------------
"""
You are given a string of length N and a parameter k. 
The string can be manipulated by taking one of the first k letters and moving it to the end.

Write a program to determine the lexicographically smallest string that can be created after an unlimited number of moves.

For example, suppose we are given the string daily and k = 1. 
The best we can create in this case is ailyd.
"""
def smallest_string_after_manipulation(string, k):
    """ return the smallest string by taking 1 of the first k letters and moving it to the end """
    if k == 0:
        return string
    letters = list(string)
    smallest_list = letters  # smallest list of letter from string initialized
    for i in range(min(k, len(string))):  # avoid OutOfBoundError of k greater than string length
        new_list = letters[:i] + letters[i+1:] + list(letters[i])  # convert i-th letter to list and move it to end of list
        if new_list < smallest_list:
            smallest_list = new_list
    smallest_string = "".join(smallest_list)
    return smallest_string

def test1():
    assert smallest_string_after_manipulation("daily", 1) == "ailyd"

def test2():
    assert smallest_string_after_manipulation("xyzabc", 6) == "xyabcz"

def test3():
    assert smallest_string_after_manipulation("abc", 6) == "abc"

if __name__ == "__main__":
    test1()
    test2()
    test3()