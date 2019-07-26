# ---------------------------------
# Author: Tuan Nguyen
# Date: 20190726
#!solutions/74.py
# ---------------------------------
"""
Suppose you have a multiplication table that is N by N. 
That is, a 2D array where the value at the i-th row and j-th column is (i + 1) * (j + 1) (if 0-indexed) or i * j (if 1-indexed).

Given integers N and X, write a function that returns the number of times X appears as a value in an N by N multiplication table.

For example, given N = 6 and X = 12, you should return 4, 
since the multiplication table looks like this:

| 1 | 2 | 3 | 4 | 5 | 6 |

| 2 | 4 | 6 | 8 | 10 | 12 |

| 3 | 6 | 9 | 12 | 15 | 18 |

| 4 | 8 | 12 | 16 | 20 | 24 |

| 5 | 10 | 15 | 20 | 25 | 30 |

| 6 | 12 | 18 | 24 | 30 | 36 |

And there are 4 12's in the table.
"""

def printMultiplicationTable(N):
# input: int N
# output: multiplication table N*N
    for i in range(N):
        r = i + 1   # row number, start from 1
        for j in range(N):
            c = j + 1   # column number, start from 1
            print(r * c, end=' ')   # print cell value, i.e product of row & column
        print("\n")


def countX_inMultiplicationTable(N, X):
# input: int N as multiplication table N*N & int X
# output: no. times X appears in multiplication table N*N
# running time: O(n^2)
    counter = 0 # init output
    for i in range(N):  # iterate in rows, max: N
        r = i + 1   # row number, start from 1
        for j in range(r):  # iteratin in columns, max: current row number
            c = j + 1   # column number, start from 1
            p = r * c   # cell value, i.e product of row & column
            if (p == X) and (r == c):  # p=X & is in diagonal of multiplication table
                counter += 1    # increase by 1
            if (p == X) and (r != c):   # p=X & is not in diagonal
                counter += 2    # increase by 2 b/c mirroring via diagonal
    return counter


def countX_inMultiplicationTable_test(N, X):
    printMultiplicationTable(N)
    print('X:', X, '~> count:', countX_inMultiplicationTable(N, X))


if __name__ == "__main__":
    countX_inMultiplicationTable_test(N=6, X=12) # return 4