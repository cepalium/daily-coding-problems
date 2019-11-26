# -------------------------
# Author: Tuan Nguyen
# Date created: 20191126
#!195.py
# -------------------------
"""
Let A be an N by M matrix in which every row and every column is sorted.

Given i1, j1, i2, and j2, compute the number of elements of A smaller than MAi1, j1] and larger than A[i2, j2].

For example, given the following matrix:
```
[[1, 3, 7, 10, 15, 20],
 [2, 6, 9, 14, 22, 25],
 [3, 8, 10, 15, 25, 30],
 [10, 11, 12, 23, 30, 35],
 [20, 25, 30, 35, 40, 45]]
```
And i1 = 1, j1 = 1, i2 = 3, j2 = 3, return 15 as there are 15 numbers in the matrix smaller than 6 or greater than 23.
"""

def num_elements(A, i1, j1, i2, j2):
    """ return number of elements of A smaller than A[i1, j1] and larger than A[i2, j2] """
    N = len(A)      # no. rows
    M = len(A[0])   # no. columns
    counter = 0     # output
    # count no. elements smaller than A[i1, j1]
    for i in range(i1):
        for j in range(M):
            if A[i][j] < A[i1][j1]: # check all elements of i1's above rows
                counter += 1
    for i in range(i1, N):
        for j in range(j1):
            if A[i][j] < A[i1][j1]: # check all elements of j1's left columns, except elements from i1's above rows (because already checked before)
                counter += 1
    # count no. elements larger than A[i2, j2]
    for i in range(i2 + 1, N):
        for j in range(M):
            if A[i][j] > A[i2][j2]: # check all elements of i2's below columns
                counter += 1
    for i in range(0, i2 + 1):
        for j in range(j2 + 1, M):
            if A[i][j] > A[i2][j2]: # check all elements of j2's right columns, except elements from i2's below rows (because already checked before)
                counter += 1
    return counter

def test_num_elements():
    A = [   [1, 3, 7, 10, 15, 20],
            [2, 6, 9, 14, 22, 25],
            [3, 8, 10, 15, 25, 30],
            [10, 11, 12, 23, 30, 35],
            [20, 25, 30, 35, 40, 45] ]
    assert(num_elements(A, 1, 1, 3, 3) == 14)

if __name__ == "__main__":
    test_num_elements()