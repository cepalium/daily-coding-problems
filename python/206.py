# ------------------------------
# Author: Tuan Nguyen
# Date created: 20191205
#!206.py
# ------------------------------
"""
A permutation can be specified by an array P, where P[i] represents the location of the element at i in the permutation. 
For example, [2, 1, 0] represents the permutation where elements at the index 0 and 2 are swapped.

Given an array and a permutation, apply the permutation to the array. 
For example, given the array ["a", "b", "c"] and the permutation [2, 1, 0], return ["c", "b", "a"].
"""

def apply_permutation_to_array(array, permutation):
    """ return the array after applying the permutation order """
    return [array[i] for i in permutation]

def test_array_permutation():
    assert apply_permutation_to_array(array=["a", "b", "c"], permutation=[2, 1, 0]) == ["c", "b", "a"]

if __name__ == "__main__":
    test_array_permutation()