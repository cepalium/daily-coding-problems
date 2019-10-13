# ---------------------------
# Author: Tuan Nguyen
# Date created: 20191013
#!solutions/153.py
# ---------------------------
"""
Find an efficient algorithm to find the smallest distance (measured in number of words) between any two given words in a string.

For example, given words "hello", and "world" and a text content of "dog cat hello cat dog dog hello cat world", 
return 1 because there's only one word "cat" in between the two words.
"""

import math


""" find the smallest distance (measured in number of words) between any two given words in a string """
def smallestDistance(string, word1, word2):
    words = string.split()      # split string input list of words
    # variables initialized
    n = len(words)
    index_word1 = math.inf
    index_word2 = math.inf
    d = math.inf            # smallest distance initialized to infinity
    # iteratively find the smallest distance through all words
    for i in range(n):
        if words[i] == word1:   # new index for word1
            index_word1 = i
        if words[i] == word2:   # new index for word2
            index_word2 = i
        if index_word1 != math.inf and index_word2 != math.inf:     # if 2 wards are found
            curDistance = abs(index_word1 - index_word2) - 1        # current distance from 2 newly-found words
            if curDistance < d:                                     # update smallest distance if it is smaller
                d = curDistance
    if d == math.inf:           # at least 1 word not exist in string
        raise IOError("One input word is not existed in string")
    return d                    # reach this, then find the smallest distance


def smallestDistance_test(string, word1, word2, desiredVal):
    print(smallestDistance(string, word1, word2) == desiredVal)


if __name__ == "__main__":
    smallestDistance_test(string="dog cat hello cat dog dog hello cat world", word1="hello", word2="world", desiredVal=1)
    smallestDistance_test(string="dog cat hello cat dog dog hello cat world", word1="dog", word2="cat", desiredVal=0)
    smallestDistance_test(string="dog cat hello cat dog dog hello cat world", word1="dog", word2="hello", desiredVal=0)
    smallestDistance_test(string="dog cat hello cat dog dog hello cat world", word1="cat", word2="hello", desiredVal=0)
    smallestDistance_test(string="dog cat hello cat dog dog hello cat world", word1="dog", word2="world", desiredVal=2)
    smallestDistance_test(string="dog cat hello cat dog dog hello cat world", word1="cat", word2="world", desiredVal=0)
    smallestDistance_test(string="dog cat hello cat dog dog hello cat world", word1="human", word2="pet", desiredVal=1)