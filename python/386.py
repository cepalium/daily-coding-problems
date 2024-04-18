# ---------------------------------
# Author: Tuan Nguyen
# Date created: 20200602
#!386.py
# ---------------------------------
"""
Given a string, sort it in decreasing order based on the frequency of characters. 
If there are multiple possible solutions, return any of them.

For example, given the string tweet, return tteew. eettw would also be acceptable.
"""


def sort_string_descending_character_frequency(string):
    if len(string) < 2:
        return string
    character_freq = character_frequency(string)
    character_frequency_pair_desc_freq = sort_dict_descending_value(
        character_freq
    )
    string_desc = make_string(character_frequency_pair_desc_freq)
    return string_desc


def character_frequency(string):
    char_freq = dict()
    for c in string:
        if char_freq.get(c, None):
            char_freq[c] += 1
        else:
            char_freq[c] = 1
    return char_freq


def sort_dict_descending_value(dictionary):
    return sorted(dictionary.items(), key=lambda item: item[1], reverse=True)


def make_string(pairs):
    string = ""
    for k, v in pairs:
        string += k * v
    return string


def test1():
    assert sort_string_descending_character_frequency("tweet") == "tteew"


if __name__ == "__main__":
    test1()
