# ------------------------------
# Author: Tuan Nguyen
# Date created: 20200112
#!211.py
# ------------------------------
"""
Given a string and a pattern, find the starting indices of all occurrences of the pattern in the string. 
For example, given the string "abracadabra" and the pattern "abr", you should return [0, 7].
"""
def starting_index(str, pat):
    """ return list of starting indices of all occurrences of the pattern in the string """
    occu = []   # output list initialized
    pivot = 0
    n = len(str)
    m = len(pat)
    if n == 0 or m == 0:      # trivial cases
        return []
    else:
        while pivot < n:
            if str[pivot] == pat[0]:
                if str[pivot:pivot+m] == pat:   # matching pattern
                    occu.append(pivot)
                    pivot += m
                else:
                    pivot += 1
            else:
                pivot += 1
        return occu

def test_starting_index():
    assert starting_index("abracadabra", "abr") == [0, 7]

if __name__ == "__main__":
    test_starting_index()