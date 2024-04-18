# -------------------------------
# Author: Tuan Nguyen
# Date created: 20190824
#!solutions/103.py
# -------------------------------
"""
Given a string and a set of characters, return the shortest substring containing all the characters in the set.

For example, given the string "figehaeci" and the set of characters {a, e, i}, you should return "aeci".

If there is no substring containing all the characters in the set, return null.
"""

import itertools


def shortestSubstring(string, characters):
    # input: string s & list chars of characters
    # output: shortest substring s.t contains all chars
    # trivial case
    if not string or not characters:
        return None
    # else
    dict_char_position = {
        c: [] for c in characters
    }  # dict {'char': [list to store index of char in string]} initialized
    # construct dict_char_position, e.g "baaa" & ['a','b'] ~> {'a':[1,2,3], 'b':[0]}
    for i in range(len(string)):
        if string[i] in characters:
            dict_char_position[string[i]].append(i)  # add index
    # construct list of (list of each char's index in string), e.g {'a':[1,2,3], 'b':[0]} ~> [[1,2,3], [0]]
    char_position_list = [v for k, v in dict_char_position.items()]
    # if 1 char doesn't appear in string ~> 1 empty sublist ~> return None
    if char_position_list.count([]):
        return None
    # else all chars appear in string
    products = itertools.product(
        *char_position_list
    )  # cartesian product, e.g [[1,2,3], [0]] ~> [[1,0], [2,0], [3,0]]
    # min substring of all chars has min distance from most-left char to most-right char
    dist = len(string) + 1  # variable dist initialized
    min_pos = 0  # initialize variable to store the most-left index
    max_pos = 0  # initialize variable to store the most-right index
    for e in products:  # check all pairs of catersian products
        tmp_dist = max(e) - min(
            e
        )  # temporary distance from most-right index to most-left index
        if (
            tmp_dist < dist
        ):  # update dist, min_pos, max_pos if smaller distance
            dist = tmp_dist
            min_pos = min(e)
            max_pos = max(e)
    return string[min_pos : max_pos + 1]


def shortestSubstring_test(s, chars):
    print("s={}, chars={} ~> {}".format(s, chars, shortestSubstring(s, chars)))


if __name__ == "__main__":
    shortestSubstring_test("figehaeci", ["a", "e", "i"])  # return "aeci"
    shortestSubstring_test("figehaeci", ["a", "b", "c"])  # return None
    shortestSubstring_test("figehaeci", ["a"])  # return "a"
    shortestSubstring_test("figehaeci", [])  # return ""
