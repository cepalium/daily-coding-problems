# -------------------------
# Author: Tuan Nguyen
# Date created: 20191019
#!159.py
# -------------------------
"""
Given a string, return the first recurring character in it, or null if there is no recurring chracter.

For example, given the string "acbbac", return "b". Given the string "abcdef", return null.
"""

def first_recur_char(str):
    """ return the first recurring character in str """
    if len(str) < 2:                        # trivial case
        return None
    char_freq_dict = {c: 0 for c in str}    # initialize all characters in str with value 0
    for c in str:                           # run though str
        char_freq_dict[c] += 1              # increase c's frequency by 1
        if char_freq_dict[c] == 2:          # if c's frequency is 2 ~> it is recurring
            return c                        # return the first recurring character
    return None                             # reach this ~> no recurring character


def firstRecurChar_test(str, desiredVal):
    assert first_recur_char(str) == desiredVal


if __name__ == "__main__":
    firstRecurChar_test(str="acbbac", desiredVal="b")
    firstRecurChar_test(str="abcdef", desiredVal=None)
    firstRecurChar_test(str="a", desiredVal=None)
    firstRecurChar_test(str="", desiredVal=None)
    firstRecurChar_test(str="aab", desiredVal="a")