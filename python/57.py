# --------------------------------
# Author: Tuan Nguyen
# Date: 20190709
#!solutions/57.py
# --------------------------------
"""
Given a string s and an integer k, 
break up the string into multiple lines such that each line has a length of k or less. 
You must break it up so that words don't break across lines. 
Each line has to have the maximum possible amount of words. 
If there's no way to break the text up, then return null.

You can assume that there are no spaces at the ends of the string 
and that there is exactly one space between each word.

For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10, 
you should return: ["the quick", "brown fox", "jumps over", "the lazy", "dog"]. 
No string in the list has a length of more than 10.
"""

def breakUpString(string, k):
# input: string 'string' and int k
# output: list of lines s.t each line has length <= k, and no word break across lines
    lines = []  # init output list of lines
    words = list(string.split())    # split input string input words
    pivot = 0
    r = pivot   # r as a forward-moving pivot 
    line = ''   # init new line of words
    while pivot <= r < len(words):
        if len(words[r]) > k:   # if a single word has length > k ~> impossible to break lines
            return None
        longerLine = line + ' ' + words[r] if line else words[r]    # try to add as many as possible words into lines
        if len(longerLine) <= k:    # if (line + next word) still has length within k
            line = longerLine
            r += 1
        else:   # if (line + next word) has length > k  
            lines.append(line)
            line = ''
            pivot = r
            r = pivot
    lines.append(line)  # add the last line
    return lines


def breakUpString_test(string, k):
    print(string, '&', k, '~>', breakUpString(string, k))


if __name__ == "__main__":
    breakUpString_test("the quick brown fox jumps over the lazy dog", k=10) # return ['the quick', 'brown fox', 'jumps over', 'the lazy', 'dog']
    breakUpString_test("the quick brown fox jumps over the lazy dog", k=5)  # return ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
    breakUpString_test("the quick brown fox jumps over the lazy dog", k=3)  # return None