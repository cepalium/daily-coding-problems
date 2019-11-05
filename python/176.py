# ------------------------
# Author: Tuan Nguyen
# Date created: 20191105
#!176.py
# ------------------------
"""
Determine whether there exists a one-to-one character mapping from one string s1 to another s2.

For example, given s1 = abc and s2 = bcd, return true since we can map a to b, b to c, and c to d.

Given s1 = foo and s2 = bar, return false since the o cannot map to two characters.
"""

def is_mapable(s1, s2):
    """ return True if possible for 1-to-1 character mapping from string s1 to s2 """
    map1to2 = {}
    n1, n2 = len(s1), len(s2)
    if n1 != n2:        # trivial case
        return False
    for char_s1, char_s2 in zip(s1, s2):
        if char_s1 not in map1to2.keys():
            map1to2[char_s1] = char_s2
        else:   # char_s1 exists
            if char_s2 != map1to2[char_s1]: # char_s1 map to 2 characters
                return False                # then not possible to map
    return True


def isMapable_test(s1, s2, desiredVal):
    assert is_mapable(s1, s2) == desiredVal


if __name__ == "__main__":
    isMapable_test(s1="abc", s2="bcd", desiredVal=True)
    isMapable_test(s1="foo", s2="bar", desiredVal=False)