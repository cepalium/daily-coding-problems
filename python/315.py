# --------------------------
# Author: Tuan Nguyen
# Date created: 20200323
#!315.py
# --------------------------
"""
In linear algebra, a Toeplitz matrix is one in which the elements on any given diagonal from top left to bottom right are identical.

Here is an example:

1 2 3 4 8
5 1 2 3 4
4 5 1 2 3
7 4 5 1 2

Write a program to determine whether a given input is a Toeplitz matrix.
"""
def is_toeplitz_matrix(matrix):
    """ return True if input matrix is a Toeplitz matrix """
    if not matrix:  # empty matrix
        return False
    n = len(matrix)  # no. rows
    m = len(matrix[0])  # no. columns
    if n == 1 or m == 1:  # trivial case: input is an vector
        return True
    # else:
    for i in range(n-1):  # all rows
        for j in range(m-1):  # all columns
            if matrix[i][j] != matrix[i+1][j+1]:  # next diagonal element is not same
                return False
    return True  # reach this -> all elements in each diagonal are equal

def test1():
    matrix = [  
        [1, 2, 3, 4, 8],
        [5, 1, 2, 3, 4],
        [4, 5, 1, 2, 3],
        [7, 4, 5, 1, 2]
        ]
    assert is_toeplitz_matrix(matrix) == True

def test2():
    matrix = [  
        [1, 2, 3],
        [5, 1, 2],
        [4, 5, 10]
        ]
    assert is_toeplitz_matrix(matrix) == False

def test3():
    matrix = [[1, 2, 3]]
    assert is_toeplitz_matrix(matrix) == True

def test4():
    matrix = [  
        [1],
        [5],
        [4]
        ]
    assert is_toeplitz_matrix(matrix) == True

def test5():
    matrix = []
    assert is_toeplitz_matrix(matrix) == False

if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()