# ------------------------
# Author: Tuan Nguyen
# Date: 20190524
# %11.py
# ------------------------
"""
Implement an autocomplete system. 
That is, given a query string s and a set of all possible query strings, 
return all strings in the set that have s as a prefix.

For example, given the query string de 
and the set of strings [dog, deer, deal], 
return [deer, deal].
"""


def autoComplete(li, s):
# input: list of strs & a query string s
# output: list of strs in the set that have s as a prefix
    queryList = []
    for str in li:
        if str[:len(s)] == s:
            queryList.append(str)
    return queryList


def autoComplete_test(li, s):
    print(li, s, autoComplete(li, s))


if __name__ == "__main__":
    autoComplete_test(['dog', 'deer', 'deal'], 'de')    # return ['deer', 'deal]