# -----------------------------
# Author: Tuan Nguyen
# Date created: 20200526
#!379.py
# -----------------------------
"""
Given a string, generate all possible subsequences of the string.

For example, given the string xyz, return an array or set with the following strings:

x
y
z
xy
xz
yz
xyz

Note that zx is not a valid subsequence since it is not in the order of the given string.
"""
def all_possible_subsequences(string):
    n = len(string)
    if n == 0:
        return []
    subsequences = []
    for i in range(1, 2**n):
        bit_map = get_inverse_bit_map(i)
        mapping_characters = get_mapping_characters(string, bit_map)
        subseq = "".join(mapping_characters)
        subsequences.append(subseq)
    return subsequences

def get_inverse_bit_map(n):
    string_bin_n = bin(n).split("b")[1]
    inverse_string_bin_n = string_bin_n[::-1]
    inverse_bit_map = [int(d) for d in inverse_string_bin_n]
    return inverse_bit_map

def get_mapping_characters(string, bit_map):
    n = min(len(string), len(bit_map))
    return [string[i] for i in range(n) if bit_map[i] == 1]


def test1():
    assert all_possible_subsequences("") == []

def test2():
    assert all_possible_subsequences("ab") == ['a', 'b', 'ab']

def test3():
    assert all_possible_subsequences("xyz") == ['x', 'y', 'xy', 'z', 'xz', 'yz', 'xyz']

if __name__ == "__main__":
    test1()
    test2()
    test3()