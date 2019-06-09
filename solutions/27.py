# ----------------------------
# Author: Tuan Nguyen
# Date: 20190609
#!solutions/27.py
# ----------------------------
"""
Given a string of round, curly, and square open and closing brackets, 
return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
"""

def isBracketBalance(str):
# input: string of brackets str
# output: True/False if the brackets are balanced
    stack = []  # init stack
    openBrackets = ['(', '[', '{']
    closingBrackets = [')', ']', '}']

    for bracket in str:
        if bracket in openBrackets:
            stack.append(bracket)
        else:   # bracket is a closing bracket
            if not stack:   # currently no open bracket in stack
                return False
            closingBracketIndex = closingBrackets.index(bracket)
            lastOpenBracketIndex = openBrackets.index(stack[-1])
            if closingBracketIndex == lastOpenBracketIndex: # 1 pair is balances
                stack.pop() # pop the last open bracket in stack
            else:
                return False

    if stack:   # stack has a open bracket in the end -> not balanced
        return False
    return True


def isBracketBalance_test(str):
    print(str, isBracketBalance(str))


if __name__ == "__main__":
    isBracketBalance_test("([])[]({})") # return True
    isBracketBalance_test("([)]") # return False
    isBracketBalance_test("((()") # return False