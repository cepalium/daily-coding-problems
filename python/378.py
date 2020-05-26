# -----------------------------
# Author: Tuan Nguyen
# Date created: 20200526
#!378.py
# -----------------------------
"""
Write a function that takes in a number, string, list, or dictionary and returns its JSON encoding. 
It should also handle nulls.

For example, given the following input:

[None, 123, ["a", "b"], {"c":"d"}]
You should return the following, as a string:

'[null, 123, ["a", "b"], {"c": "d"}]'
"""
import json

def test1():
    assert json.dumps(123) == "123"

def test2():
    assert json.dumps(["a", "b"]) == '''["a", "b"]'''

def test3():
    assert json.dumps([None, 123, ["a", "b"], {"c": "d"}]) == '''[null, 123, ["a", "b"], {"c": "d"}]'''

if __name__ == "__main__":
    test1()
    test2()
    test3()