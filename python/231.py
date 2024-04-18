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
    """return a string s.t no 2 adjacent characters from input string are the same"""
    n = len(str)
    if n == 1:  # trivial case
        return str

    char_lst = list(
        str
    )  # list data structure for pop/add methods in O(1) time
    pivot = 1
    while pivot < n:
        time_out = 0  # in case pivot cannot reach end of list due to all the rest of characters are the same, time-out to break the while-loop and return None
        if (
            pivot == n - 1 and char_lst[pivot] == char_lst[pivot - 1]
        ):  # end of string and impossible to rearrange
            return None
        while char_lst[pivot] == char_lst[pivot - 1]:
            if (
                time_out == n - pivot
            ):  # time-out: the first same character is swapping back to pivot position
                return None
            char_lst.append(
                char_lst.pop(pivot)
            )  # push the same character to end of list
            time_out += 1
        pivot += 1
    return "".join(char_lst)


def test_rearrange():
    assert rearrange("aaabbc") == "abcaba"
    assert rearrange("aaab") == None
    assert rearrange("aaaab") == None
    assert rearrange("aaaa") == None


if __name__ == "__main__":
    test_rearrange()
