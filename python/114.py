# --------------------------
# Author: Tuan Nguyen
# Date created: 20190904
#!solutions/114.py
# --------------------------
"""
Given a string and a set of delimiters, reverse the words in the string 
while maintaining the relative order of the delimiters. 
For example, given "hello/world:here", return "here/world:hello"

Follow-up: Does your solution work for the following cases: "hello/world:here/", "hello//world:here"
"""

# constant variables
DELIMITERS = ["/", ":", " ", ",", "."]


def reverseWords(string, delim):
    # input: a string & a set of delimiters delim
    # output: a string s.t reverse the words in string while keep the relative order of delimiters
    # running time: O(n)
    # instance variables
    marker = 0  # all the elements before this index has been checked
    pivot = 0  # keep increasing to check the char in input string
    delimiterFlag = False  # delimiter flag to check the current sequence of characters is word or delimiter
    words = []  # list of words from input string
    delimiters = []  # list of delimiters from input string
    startByWord = (
        True if string[0] not in delim else False
    )  # to identify the order of merging: word if True, delim if False
    i_words = 0  # iterator in list words
    i_delimiters = 0  # iterator in list delimiters
    output = []  # list of reversed words & relative-ordered delimiters
    # separate words and delimiters in order from input string
    while pivot < len(string):
        if (not delimiterFlag) and (
            string[pivot] not in delim
        ):  # continue sequence of chars that makes up a word
            pivot += 1
        elif (not delimiterFlag) and (
            string[pivot] in delim
        ):  # end of current word, start of new delimiter
            words.append(string[marker:pivot])  # add new word into list words
            marker = pivot  # update marker
            pivot += 1
            delimiterFlag = True  # update flag
        elif (delimiterFlag) and (
            string[pivot] not in delim
        ):  # end of current delimiter, start of new word
            delimiters.append(
                string[marker:pivot]
            )  # add new delimiter into list delimiters
            marker = pivot  # update marker
            pivot += 1
            delimiterFlag = False  # update flag
        else:  # continue sequence of chars that makes up a delimiter
            pivot += 1
    # add the last sequence of characters to according list based on delimiter flag
    if delimiterFlag:
        delimiters.append(string[marker:pivot])
    else:
        words.append(string[marker:pivot])
    # reverse list of words
    words = words[::-1]
    # merge reversed words and delimiters while maintaining the relative order of the delimiters.
    while (i_words < len(words)) and (i_delimiters < len(delimiters)):
        if startByWord:
            output.append(words[i_words])  # add word to output
            i_words += 1  # move iterator
        else:
            output.append(delimiters[i_delimiters])  # add delimiter to output
            i_delimiters += 1  # move iterator
        startByWord = (
            not startByWord
        )  # reverse to add element from the other list at next round
    # copy the rest to output
    while i_words < len(words):
        output.append(words[i_words])
        i_words += 1
    while i_delimiters < len(delimiters):
        output.append(delimiters[i_delimiters])
        i_delimiters += 1
    return "".join(output)  # list to string


def reverseWords_test(string, delim):
    print("{} ~> reversed: {}".format(string, reverseWords(string, delim)))


if __name__ == "__main__":
    reverseWords_test(
        "hello/world:here", DELIMITERS
    )  # print "here/world:hello"
    reverseWords_test(
        "hello/world:here/", DELIMITERS
    )  # print "here/world:hello/"
    reverseWords_test(
        "hello//world:here", DELIMITERS
    )  # print "here//world:hello"
    reverseWords_test("/abc//ijk:xyz:", DELIMITERS)  # print "/xyz//ijk:abc:"
