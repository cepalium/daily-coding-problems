# --------------------------
# Author: Tuan Nguyen
# Date created: 20191130
#!201.py
# --------------------------
"""
You are given an array of arrays of integers, where each array corresponds to a row in a triangle of numbers. 
For example, [[1], [2, 3], [1, 5, 1]] represents the triangle:
  1
 2 3
1 5 1
We define a path in the triangle to start at the top and go down one row at a time to an adjacent value, 
eventually ending with an entry on the bottom row. 
For example, 1 -> 3 -> 5. The weight of the path is the sum of the entries.

Write a program that returns the weight of the maximum weight path.
"""


def max_weight_path(lst):
    """returns the weight of the maximum weight path; path is from top to bottom level"""
    n = len(lst)  # no. levels from top node
    weight = [
        [0] * (i + 1) for i in range(n)
    ]  # max accumulative weight at each node initialized
    for i in range(n):  # go through each leval
        for j in range(i + 1):  # go through each node: level i has i+1 nodes
            if (
                j == 0
            ):  # leftmost node: its parent is previous level's leftmost node
                weight[i][j] = lst[i][j] + weight[i - 1][j]
            elif (
                j == i
            ):  # rightmost node: its parent is previous level's rightmost node
                weight[i][j] = lst[i][j] + weight[i - 1][j - 1]
            else:  # in-between nodes: it has 2 parents node, pick max
                weight[i][j] = lst[i][j] + max(
                    weight[i - 1][j - 1], weight[i - 1][j]
                )
    return max(weight[n - 1])  # return max value of bottom level


def test_max_weight_path():
    assert max_weight_path([[1], [2, 3], [1, 5, 1]]) == 9


if __name__ == "__main__":
    test_max_weight_path()
