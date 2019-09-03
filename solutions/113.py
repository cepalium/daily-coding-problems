# -----------------------------
# Author: Tuan Nguyen
# Date created: 20190903
#!solutions/113.py
# -----------------------------
"""
Given a string of words delimited by spaces, reverse the words in string. 
For example, given "hello world here", return "here world hello"

Follow-up: given a mutable string representation, can you perform this operation in-place?
"""

def reverseBySpace(string):
# input: string of words delimited by spaces
# output: a reversed string of words
    return ' '.join(string.split()[::-1])   # join with spaces the reversed list of string split by spaces 


def reverseBySpace_test(string):
    print(string, '~>', reverseBySpace(string))


if __name__ == "__main__":
    reverseBySpace_test("hello world here") # print "here world hello"
