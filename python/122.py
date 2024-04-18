# -----------------------
# Author: Tuan Nguyen
# Date created: 20190918
#!solutions/122.py
# -----------------------
"""
You are given a 2-d matrix where each cell represents number of coins in that cell. 
Assuming we start at matrix[0][0], and can only move right or down, 
find the maximum number of coins you can collect by the bottom right corner.

For example, in this matrix
0 3 1 1
2 0 0 4
1 5 3 1

The most we can collect is 0 + 2 + 1 + 5 + 3 + 1 = 12 coins.
"""


def maxNumberCoins(matrix):
    # input: 2D array of int
    # output: max no. coins can be collected from matrix[0][0] to bottom right corner by only moving right or down
    # method: dynamic programming
    # running time: O(n*m), where n=no. rows, m=no. columns in matrix
    # instance variables
    n_rows = len(matrix)
    n_cols = len(matrix[0])
    # output matrix initialized
    sumCoins = [[0 for j in range(n_cols)] for i in range(n_rows)]
    # iteration:
    # Bellman's equation: sumCoins[i][j] = matrix[i][j] + max{0, sumCoins[i][j-1], sumCoins[i-1][j]}
    for i in range(n_rows):
        for j in range(n_cols):
            if (i == 0) and (j == 0):  # base case: position [0][0]
                sumCoins[i][j] = matrix[i][j]
            elif (i == 0) and (j != 0):  # 1st row, but exclude [0][0]
                sumCoins[i][j] = matrix[i][j] + sumCoins[i][j - 1]
            elif (i != 0) and (j == 0):  # 1st column, but exclude [0][0]
                sumCoins[i][j] = matrix[i][j] + sumCoins[i - 1][j]
            else:
                sumCoins[i][j] = matrix[i][j] + max(
                    [sumCoins[i][j - 1], sumCoins[i - 1][j]]
                )
    return sumCoins[n_rows - 1][
        n_cols - 1
    ]  # return no. coins at bottom right corner position


def maxNumberCoins_test(matrix, desiredVal):
    for row in matrix:
        print(row)
    print(desiredVal, maxNumberCoins(matrix) == desiredVal)


if __name__ == "__main__":
    maxNumberCoins_test(
        matrix=[[0, 3, 1, 1], [2, 0, 0, 4], [1, 5, 3, 1]], desiredVal=12
    )  # print True
