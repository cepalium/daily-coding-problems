# ------------------------
# Author: Tuan Nguyen
# Date created: 20191102
#!172.py
# ------------------------
"""
Given a string s and a list of words words, where each word is the same length, 
find all starting indices of substrings in s that is a concatenation of every word in words exactly once.

For example, given s = "dogcatcatcodecatdog" and words = ["cat", "dog"], 
return [0, 13], since "dogcat" starts at index 0 and "catdog" starts at index 13.

Given s = "barfoobazbitbyte" and words = ["dog", "cat"], 
return [] since there are no substrings composed of "dog" and "cat" in s.

The order of the indices does not matter.
"""

from itertools import permutations

def starting_indices(s, words):
    """ all starting indices of substrings in s that is a concatenation of every word in words exactly once. """
    first_char = [word[0] for word in words]
    word_concat = [''.join(combo) for combo in permutations(words)]
    n = len(s)                  # s's length
    m = len(word_concat[0])     # word concatenation's length
    i = 0
    index_list = []             # output list
    while i < n-m+1:                # go through s
        if s[i] in first_char:      # if current char match 1st char of any word in words
            piece = s[i:i+m] 
            if piece in word_concat:    # if this slice is a word concatenation
                index_list.append(i)    # add current cursor to output list
                word_concat.remove(piece)   # make sure exactly once of this concatenation
                i += m                      # jump cursor
                continue
        i += 1  # else, move cursor to left by 1 position
    return index_list


if __name__ == "__main__":
    assert starting_indices(s="dogcatcatcodecatdog", words=["cat", "dog"]) == [0, 13]
    assert starting_indices(s="barfoobazbitbyte", words=["cat", "dog"]) == []