# ----------------------------
# Author: Tuan Nguyen
# Date created: 20191128
#!199.py
# ----------------------------
"""
Given a string of parentheses, find the balanced string that can be produced from it using the minimum number of insertions and deletions. 
If there are multiple solutions, return any of them.

For example, given "(()", you could return "(())". 
Given "))()(", you could return "()()()()".
"""

def balance_string(str):
    """ return the balanced string that can be produced from it 
    using the minimum number of insertions and deletions"""
    L = list(str)                           # array of parentheses from input str ~> insert balanced parentheses into L ~> output = string of L
    stack = list()                          # stack of unmatched parentheses
    for i, c in enumerate(str):
        if c == "(":
            stack.append((i, c))
        elif not stack and c == ")":        # empty stack & c is ")"
            stack.append((i, c))        
        elif stack and stack[-1][1] == ")": # last bracket in stack is ")" & c is also ")"
            stack.append((i, c))
        else:                               # last bracket in stack is "(" & c is ")" ~> balanced pair
            stack.pop()
    while len(stack) > 0:                   # balance unmatched parentheses
        last_item = stack.pop()
        i, c = last_item[0], last_item[1]
        if c == "(":                        # balance "(": add ")" after it
            L.insert(i + 1, ")")
        else:                               # balance ")": add "(" before it
            L.insert(i, "(")
    return ''.join(L)

def test_balance_string():
    assert balance_string("(()") == "()()"
    assert balance_string("))()(") == "()()()()"

if __name__ == "__main__":
    test_balance_string()