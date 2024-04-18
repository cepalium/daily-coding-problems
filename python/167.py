# -----------------------
# Author: Tuan Nguyen
# Date created: 20191027
#!167.py
# -----------------------
"""
Given a list of words, find all pairs of unique indices 
such that the concatenation of the two words is a palindrome.

For example, given the list ["code", "edoc", "da", "d"], return [(0, 1), (1, 0), (2, 3)].
"""


def all_palindrome_pairs(lst):
    """return a list of all pairs of unique indices
    such that the concatenation of the two words is a palindrome"""
    pairs = []  # output list initialized
    n = len(lst)
    for i, word_i in enumerate(lst):
        for j, word_j in enumerate(lst):
            if i != j and is_palindrome(word_i + word_j):
                pairs.append((i, j))  # add pair of unique indices
    return pairs


def is_palindrome(word):
    """return True if word is palindrome"""
    n = len(word)
    for i in range(n // 2):
        if word[i] != word[-1 - i]:  # left char doesn't match with right char
            return False
    return True  # reach this ~> palindrome word


def test_allPalindromePairs():
    assert all_palindrome_pairs(["code", "edoc", "da", "d"]) == [
        (0, 1),
        (1, 0),
        (2, 3),
    ]


if __name__ == "__main__":
    test_allPalindromePairs()
