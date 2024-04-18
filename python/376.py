# ----------------------------------
# Author: Tuan Nguyen
# Date created: 20200524
#!376.py
# ----------------------------------
"""
You are writing an AI for a 2D map game. 
You are somewhere in a 2D grid, and there are coins strewn about over the map.

Given the position of all the coins and your current position, 
find the closest coin to you in terms of Manhattan distance. 
That is, you can move around up, down, left, and right, but not diagonally. 
If there are multiple possible closest coins, return any of them.

For example, given the following map, where you are x, 
coins are o, and empty spaces are . (top left is 0, 0):

---------------------
| . | . | x | . | o |
---------------------
| o | . | . | . | . |
---------------------
| o | . | . | . | o |
---------------------
| . | . | o | . | . |
---------------------

return (0, 4), since that coin is closest. 
This map would be represented in our question as:

Our position: (0, 2)
Coins: [(0, 4), (1, 0), (2, 0), (3, 2)]
"""


def closest_coin(position, coins):
    n = len(coins)
    if n == 0:
        return None
    min_distance = get_manhattan_distance(position, coins[0])  # initialize
    closest = coins[0]
    for i in range(1, n):
        d = get_manhattan_distance(position, coins[i])
        if d < min_distance:
            min_distance = d
            closest = coins[i]
    return closest


def get_manhattan_distance(p1, p2):
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    return abs(x1 - x2) + abs(y1 - y2)


def test1():
    assert closest_coin(
        position=(0, 2), coins=[(0, 4), (1, 0), (2, 0), (3, 2)]
    ) == (
        0,
        4,
    )


if __name__ == "__main__":
    test1()
