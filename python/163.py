# -------------------------
# Author: Tuan Nguyen
# Date created: 20191023
#!163.py
# -------------------------
"""
Given an arithmetic expression in Reverse Polish Notation, write a program to evaluate it.

The expression is given as a list of numbers and operands. For example: [5, 3, '+'] should return 5 + 3 = 8.

For example, [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-'] should return 5, 
since it is equivalent to ((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) = 5.

You can assume the given expression is always valid.
"""

def reverse_polish_expression(exp):
    """ evaluate a list of numbers and operands in Reverse Polish Notation """
    stack = []                          # stack of numbers initialized
    for e in exp:                       # go through expression in 1 scan ~> running time: O(n)
        if not isinstance(e, str):           # current element is numeric
            stack.append(e)
        else:                           # current element is operand
            number1 = stack.pop()
            number2 = stack.pop()
            piece = eval(str(number2) + e + str(number1))   # calculate a small piece in arithmetic exp
            stack.append(piece)
    return stack.pop()  # the only (and last) element in stack is final result


def test_reversePolishExpression():
    assert reverse_polish_expression([15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']) == 5


if __name__ == "__main__":
    test_reversePolishExpression()