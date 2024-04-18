# ----------------------------
# Author: Tuan Nguyen
# Date created: 20200222
#!285.py
# ----------------------------
"""
You are given an array representing the heights of neighboring buildings on a city street, from east to west. 
The city assessor would like you to write an algorithm that returns how many of these buildings have a view of the setting sun, in order to properly value the street.

For example, given the array [3, 7, 8, 3, 6, 1], you should return 3, since the top floors of the buildings with heights 8, 6, and 1 all have an unobstructed view to the west.

Can you do this using just one forward pass through the array?
"""


def building_view_sunset(building_heights):
    """return number of buildings which have a view of sunset"""
    n = len(building_heights)
    if n == 0:  # trivial cases
        return 0
    if n == 1:
        return 1
    max_height = [0 for i in range(n)]
    max_height[n - 1] = building_heights[
        n - 1
    ]  # rightmost building can always view the sunset
    num_buildings = (
        1  # output initialized. Rightmost building can always view the sunset
    )
    for i in range(n - 2, -1, -1):  # iterate from west to east
        # dynamic programming: max_height[i] = max(building_heights[i], max_height[i+1])
        if building_heights[i] > max_height[i + 1]:
            num_buildings += 1
            max_height[i] = building_heights[i]
        else:
            max_height[i] = max_height[i + 1]
    return num_buildings


def test1():
    assert building_view_sunset([3, 7, 8, 3, 6, 1]) == 3


def test2():
    assert building_view_sunset([]) == 0


def test3():
    assert building_view_sunset([1]) == 1


def test4():
    assert building_view_sunset([5, 4, 3, 2, 1]) == 5


def test5():
    assert building_view_sunset([1, 2, 3, 4, 5]) == 1


if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()
