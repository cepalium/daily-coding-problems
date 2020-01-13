# -----------------------------
# Author: Tuan Nguyen
# Date created: 20200113
#!231.py
# -----------------------------
"""
Given a string with repeated characters, rearrange the string so that no two adjacent characters are the same. 
If this is not possible, return None.

For example, given "aaabbc", you could return "ababac". 
Given "aaab", return None.
"""
def rearrange(str):
    """ return a string s.t no 2 adjacent characters from input string are the same """
    char_lst = list(str)    # list data structure for pop/add methods in O(1) time
    n = len(str)
    pivot = 1
    while pivot < n:
        if pivot == n-1 and char_lst[pivot] == char_lst[pivot-1]:   # end of string and impossible to rearrange
            return None
        if char_lst[pivot] == char_lst[pivot-1]:
            char_lst.append(char_lst.pop(pivot))    # push the same character to end of list
        else:
            pivot += 1
    return ''.join(char_lst)

def test_rearrange():
    assert rearrange("aaabbc") == "abcaba"
    assert rearrange("aaab") == None

if __name__ == "__main__":
    test_rearrange()