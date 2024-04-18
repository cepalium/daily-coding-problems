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


""" find the smallest distance (measured in number of words) between any two given words in a string """


def smallestDistance(string, word1, word2):
    # running time: O(n)
    words = string.split()  # split string input list of words
    # variables initialized
    n = len(words)
    index_word1 = None
    index_word2 = None
    d = None  # smallest distance variable
    # iteratively find the smallest distance through all words
    for i in range(n):
        if words[i] == word1:  # new index for word1
            index_word1 = i
        if words[i] == word2:  # new index for word2
            index_word2 = i
        if index_word1 and index_word2:  # if 2 words are found up till now
            curDistance = (
                abs(index_word1 - index_word2) - 1
            )  # current distance from 2 newly-found words
            if (
                d is None or curDistance < d
            ):  # update smallest distance if it is smaller
                d = curDistance

    if d is None:  # at least 1 word not exist in string
        raise IOError("One input word is not existed in string")
    return d  # reach this, then smallest distance found


def smallestDistance_test(string, word1, word2, desiredVal):
    print(smallestDistance(string, word1, word2) == desiredVal)


if __name__ == "__main__":
    smallestDistance_test(
        string="dog cat hello cat dog dog hello cat world",
        word1="hello",
        word2="world",
        desiredVal=1,
    )
    smallestDistance_test(
        string="dog cat hello cat dog dog hello cat world",
        word1="dog",
        word2="cat",
        desiredVal=0,
    )
    smallestDistance_test(
        string="dog cat hello cat dog dog hello cat world",
        word1="dog",
        word2="hello",
        desiredVal=0,
    )
    smallestDistance_test(
        string="dog cat hello cat dog dog hello cat world",
        word1="cat",
        word2="hello",
        desiredVal=0,
    )
    smallestDistance_test(
        string="dog cat hello cat dog dog hello cat world",
        word1="dog",
        word2="world",
        desiredVal=2,
    )
    smallestDistance_test(
        string="dog cat hello cat dog dog hello cat world",
        word1="cat",
        word2="world",
        desiredVal=0,
    )
