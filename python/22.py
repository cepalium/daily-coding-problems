# --------------------------------
# Author: Tuan Nguyen
# Date: 20190604
#!solutions/22.py
# --------------------------------
"""
Given a dictionary of words and a string made up of those words (no spaces), 
return the original sentence in a list. 
If there is more than one possible reconstruction, return any of them. 
If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", 
you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", 
return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
"""


def reconstructSentence(s, words):
    # input: string 's' & list 'words' of words
    # output: list of words constructing string s if all words in l
    reconstructWords = []  # init output list if reconstructing successfully
    pivot = 0
    while pivot <= len(s):
        if (
            s[:pivot] in words
        ):  # check if from s[0] to s[pivot] match any word in words
            reconstructWords.append(s[:pivot])
            s = s[pivot:]  # substract word from input string
            pivot = 0  # begin process again
        else:
            pivot += 1
    if not s:  # s is reconstructed successfully
        return reconstructWords
    return []


def reconstructSentence_test(s, words):
    print(s, reconstructSentence(s, words))


if __name__ == "__main__":
    reconstructSentence_test(
        "thequickbrownfox", ["quick", "brown", "the", "fox"]
    )  # return ['the', 'quick', 'brown', 'fox']
    reconstructSentence_test(
        "bedbathandbeyond", ["bed", "bath", "bedbath", "and", "beyond"]
    )  # return ['bed', 'bath', 'and', 'beyond]
    reconstructSentence_test("abc", ["d", "e", "f"])  # return []
