# ----------------------------------
# Author: Tuan Nguyen
# Date: 20190607
#!solutions/25.py
# ----------------------------------
"""
Implement regular expression matching with the following special characters:

'.' (period) which matches any single character <br/>
'*' (asterisk) which matches zero or more of the preceding element
That is, implement a function that takes in a string and a valid regular expression 
and returns whether or not the string matches the regular expression.

For example, given the regular expression "ra." and the string "ray", 
your function should return true. 
The same regular expression on the string "raymond" should return false.

Given the regular expression ".*at" and the string "chat", 
your function should return true. 
The same regular expression on the string "chats" should return false.
"""


def regexMatch(string, pattern):
    # input: 2 strings string & pattern (pattern w/ rules of "." and "*")
    # output: True/False if string matches w/ pattern
    pivot = 0
    for i in range(len(pattern)):
        if (
            (i == len(pattern) - 1)
            and (0 < pivot < len(string) - 1)
            and (pattern[i] != "*")
        ):  # end of pattern but string still has character(s) which is not "*"
            return False
        if pattern[i] == ".":  # '.' matches any single character
            pivot += 1
            continue
        if pattern[i] == "*":  # '*' matches >=0 preceding elements
            # skip pivot to the remained character index in pattern
            # e.g pattern "ab*cd" -> after "*" in pattern, there remains 2 characters left -> pivot in string = -2
            # no. characters left in pattern = len(pattern) - 1 - i
            pivot = i + 1 - len(pattern)
            continue
        if string[pivot] != pattern[i]:  # normal case: not match a character
            return False
        else:
            pivot += 1
            continue
    return True


def regexMatch_test(string, pattern):
    print(string, pattern, regexMatch(string, pattern))


if __name__ == "__main__":
    regexMatch_test(string="ray", pattern="ra.")  # return True
    regexMatch_test(string="raymond", pattern="ra.")  # return False
    regexMatch_test(string="chat", pattern=".*at")  # return True
    regexMatch_test(string="chats", pattern=".*at")  # return False
