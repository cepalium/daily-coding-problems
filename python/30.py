# ---------------------------------------------
# Author: Tuan Nguyen
# Date: 20190612
#!solutions/30.py
# ---------------------------------------------
"""
You are given an array of non-negative integers 
that represents a two-dimensional elevation map 
where each element is unit-width wall 
and the integer is the height. 
Suppose it will rain and all spots between two walls get filled up.

Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.

Given the input [3, 0, 1, 3, 0, 5], 
we can hold 3 units in the first index, 
2 in the second, and 3 in the fourth index (we cannot hold 5 since it would run off to the left), 
so we can trap 8 units of water.
"""


def waterRemain(walls):
    # input: array map of non-negative ints
    # output: no. water unites remain trapped on the map
    water = 0  # init output
    firstWall = walls[0]  # 1st wall
    restHighest = max(walls[1:])  # highest wall apart from the 1st wall
    heightLimit = min(
        [firstWall, restHighest]
    )  # smaller one from 1st wall the restHighest
    i = 1
    while (
        i < len(walls) - 1
    ):  # water fills to n-1 wall, i.e last wall not count
        water += heightLimit - walls[i]
        if walls[i] == restHighest:  # adjust params again
            firstWall = restHighest
            restHighest = max(walls[walls.index(restHighest) + 1 :])
            heightLimit = min([firstWall, restHighest])
        i += 1
    return water


def waterRemain_test(walls):
    print(walls, waterRemain(walls))


if __name__ == "__main__":
    waterRemain_test([2, 1, 2])  # return 1
    waterRemain_test([3, 0, 1, 3, 0, 5])  # return 8
    waterRemain_test([3, 2, 1, 0, 1, 2, 3])  # return 9
    waterRemain_test([3, 0, 1, 2, 0, 1])  # return 4
