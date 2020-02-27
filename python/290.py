# --------------------------
# Author: Tuan Nguyen
# Date created: 20200228
#!290.py
# --------------------------
"""
On a mysterious island there are creatures known as Quxes which come in three colors: red, green, and blue. 
One power of the Qux is that if two of them are standing next to each other, they can transform into a single creature of the third color.

Given N Quxes standing in a line, determine the smallest number of them remaining after any possible sequence of such transformations.

For example, given the input ['R', 'G', 'B', 'G', 'B'], it is possible to end up with a single Qux through the following steps:

        Arrangement       |   Change
----------------------------------------
['R', 'G', 'B', 'G', 'B'] | (R, G) -> B
['B', 'B', 'G', 'B']      | (B, G) -> R
['B', 'R', 'B']           | (R, B) -> G
['B', 'G']                | (B, G) -> R
['R']                     |
"""
def quxes_tranformation(quxes):
    """ return the smallest number of Quxes remaining after the transformation """
    if len(quxes) == 0:    # trivial case
        return 0
    if len(quxes) == 1:
        return 1
    transformed = []    # queue of after-transformed Quxes
    while quxes:
        top_qux = quxes.pop(0)
        while transformed and transformed[-1] != top_qux:    # loop: transform 2 different neighboring quxes
            last_transformed = transformed.pop()
            top_qux = new_qux(top_qux, last_transformed)
        transformed.append(top_qux)
    return len(transformed)

def new_qux(a, b):
    """ return the merged Qux from 2 input Quxes a & b """
    quxes = ['R', 'G', 'B']
    quxes.remove(a)
    quxes.remove(b)
    return quxes[0]

# ------ UNIT TEST ------
def test1():
    assert quxes_tranformation(['R', 'G', 'B', 'G', 'B']) == 1

def test2():
    assert quxes_tranformation(['R', 'G', 'B']) == 2

def test3():
    assert quxes_tranformation([]) == 0

def test4():
    assert quxes_tranformation(['R']) == 1

def test5():
    assert quxes_tranformation(['R', 'R', 'R']) == 3

if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()