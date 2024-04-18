# --------------------------
# Author: Tuan Nguyen
# Date created: 20200401
#!324.py
# --------------------------
"""
Consider the following scenario: there are N mice and N holes placed at integer points along a line. 
Given this, find a method that maps mice to holes such that the largest number of steps any mouse takes is minimized.

Each move consists of moving one mouse one unit to the left or right, and only one mouse can fit inside each hole.

For example, suppose the mice are positioned at [1, 4, 9, 15], and the holes are located at [10, -5, 0, 16]. 
In this case, the best pairing would require us to send the mouse at 1 to the hole at -5, so our function should return 6.
"""


def min_mouse_step(mice, holes):
    """return the minimized largest number of steps any mouse must take to fill each hole"""
    N = len(mice)
    if N == 0:  # trivial case
        return 0
    # mouse at index i should go to the hole at index i
    mice.sort()
    holes.sort()
    largest_steps = -1
    # find the max steps that a mouse takes to its corresponding hole
    for i in range(N):
        if abs(mice[i] - holes[i]) > largest_steps:
            largest_steps = abs(mice[i] - holes[i])
    return largest_steps


def test1():
    assert min_mouse_step(mice=[1, 4, 9, 15], holes=[10, -5, 0, 16]) == 6


def test2():
    assert min_mouse_step(mice=[], holes=[]) == 0


def test3():
    assert min_mouse_step(mice=[1, 2, 3], holes=[4, 5, 6]) == 3


if __name__ == "__main__":
    test1()
    test2()
    test3()
