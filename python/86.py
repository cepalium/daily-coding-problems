# -----------------------------
# Author: Tuan Nguyen
# Date: 20190807
#!solutions/86.py
# -----------------------------
"""
Given a string of parentheses, 
write a function to compute the minimum number of parentheses to be removed to make the string valid 
(i.e. each open parenthesis is eventually closed).

For example, given the string "()())()", you should return 1. 
Given the string ")(", you should return 2, since we must remove all of them.
"""

validPair = "()"


def numberRemovedParentheses(s):
    # input: 1 string 's' of parentheses
    # output: min no. removed parentheses to make 's' valid
    # running time: O(n)
    # method: stack
    # trivial case:
    if len(s) == 0:
        return 0
    # else:
    stack = (
        []
    )  # init stack ~> store invalid parentheses which need to be removed
    p = 0  # init pivot
    # loop through input string 's'
    while p < len(s):
        stack.append(s[p])  # add current parenthesis of 's' into stack
        p += 1  # increase pivot to continue loop
        # check if the newly-added parenthesis makes a valid pair w/ the previous one
        # if yes, pop the last 2 parentheses from stack
        if (len(stack) > 1) and (str(stack[-2] + stack[-1]) == validPair):
            stack.pop()
            stack.pop()
    return len(stack)


def numberRemovedParentheses_test(s):
    print("{} ~> {}".format(s, numberRemovedParentheses(s)))


if __name__ == "__main__":
    numberRemovedParentheses_test(s="()())()")  # return 1
    numberRemovedParentheses_test(s=")(")  # return 2
    numberRemovedParentheses_test(s=")")  # return 1
    numberRemovedParentheses_test(s="")  # return 0
    numberRemovedParentheses_test(s="(((())))")  # return 0
    numberRemovedParentheses_test(s="(((()))))")  # return 1
