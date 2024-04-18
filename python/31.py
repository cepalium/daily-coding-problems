# ---------------------------------------
# Author: Tuan Nguyen
# Date: 20190613
#!solutions/31.py
# --------------------------------------
"""
The edit distance between two strings refers to the minimum number of character 
insertions, deletions, and substitutions required to change one string to the other. 
For example, the edit distance between “kitten” and “sitting” is three: 
substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.
"""


def minEditDistance(x, y):
    # input: 2 strings x & y
    # output: minimum edit distance from x to y
    # method: dynamic programming
    col_x = len(x) + 1
    row_y = len(y) + 1
    editMatrix = [
        [0 for i in range(row_y)] for j in range(col_x)
    ]  # init edit distance matrix
    # base case:
    editMatrix[0] = [i for i in range(row_y)]
    for i in range(col_x):
        editMatrix[i][0] = i
    # Bellman's equation:
    for i in range(1, col_x):
        for j in range(1, row_y):
            diff = editMatrix[i - 1][j - 1]
            if x[i - 1] != y[j - 1]:  # different
                diff += 1
            insert = editMatrix[i][j - 1] + 1
            delete = editMatrix[i - 1][j] + 1
            editMatrix[i][j] = min([diff, insert, delete])
    return editMatrix[-1][-1]  # return last element of editMatrix


def minEditDistance_test(x, y):
    print(x, y, minEditDistance(x, y))


if __name__ == "__main__":
    minEditDistance_test("kitten", "sitting")  # return 3
    minEditDistance_test("snowy", "sunny")  # return 3
    minEditDistance_test("begin", "end")  # return 4
