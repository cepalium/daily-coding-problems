# -------------------------------
# Author: Tuan Nguyen
# Date created: 20200613
#!395.py
"""
Given an array of strings, group anagrams together.

For example, given the following array:

['eat', 'ate', 'apt', 'pat', 'tea', 'now']

Return:

[['eat', 'ate', 'tea'],
 ['apt', 'pat'],
 ['now']]
"""
def group_anagrams(strings):
    anagram_dict = dict()
    for s in strings:
        sorted_chars = sorted(s)
        s_sorted = "".join(sorted_chars)
        if anagram_dict.get(s_sorted, None):
            anagram_dict[s_sorted].append(s)
        else:
            anagram_dict[s_sorted] = [s]
    return list(anagram_dict.values())


def test1():
    assert group_anagrams(['eat', 'ate', 'apt', 'pat', 'tea', 'now']) \
        == [['eat', 'ate', 'tea'], ['apt', 'pat'], ['now']]

if __name__ == "__main__":
    test1()