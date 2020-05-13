# -------------------------------
# Author: Tuan Nguyen
# Date created: 20200513
#!366.py
# -------------------------------
"""
Given a string s, rearrange the characters so that any two adjacent characters are not the same. 
If this is not possible, return null.

For example, if s = yyz then return yzy. If s = yyy then return null.
"""
def rearrange(s):
    if not s:
        return None
    rearranged = []
    letters = list(s)
    rearranged.append(letters.pop(0))  # reaaranged string starts with 1st letter of original string
    while letters:
        last_letter_in_rearranged = rearranged[-1]
        i = get_index_of_first_different_letter(letters, last_letter_in_rearranged)
        if i == -1:
            return None
        rearranged.append(letters.pop(i))  # else case
    return "".join(rearranged)

def get_index_of_first_different_letter(letters, reference_letter):
    n = len(letters)
    for i in range(n):
        if letters[i] != reference_letter:
            return i
    return -1  # all letters are the same as reference letter


def test1():
    assert rearrange("yyz") == "yzy"

def test2():
    assert rearrange("yyy") == None

if __name__ == "__main__":
    test1()
    test2()