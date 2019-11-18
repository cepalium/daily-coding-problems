# ----------------------
# Author: Tuan Nguyen
# Date created: 20191118
#!168.py
# ----------------------
"""
Given an N by N matrix, rotate it by 90 degrees clockwise.

For example, given the following matrix:

[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
you should return:

[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
Follow-up: What if you couldn't use any extra space?
"""

def rotate(matrix):
    """ return a 90-degree-rotated N*N matrix """
    n = len(matrix)
    return [ [matrix[n-j-1][i] for j in range(n)] for i in range(n) ]

def test_rotate():
    assert rotate([ [1, 2, 3],[4, 5, 6],[7, 8, 9] ]) == [ [7, 4, 1],[8, 5, 2],[9, 6, 3] ]

if __name__ == "__main__":
    test_rotate()

