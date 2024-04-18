# -----------------------------
# Author: Tuan Nguyen
# Date created: 20190822
#!solutions/100.py
# -----------------------------
"""
You are in an infinite 2D grid where you can move in any of the 8 directions:
 (x,y) to
    (x+1, y),
    (x - 1, y),
    (x, y+1),
    (x, y-1),
    (x-1, y-1),
    (x+1,y+1),
    (x-1,y+1),
    (x+1,y-1)

You are given a sequence of points and the order in which you need to cover the points. 
Give the minimum number of steps in which you can achieve it. You start from the first point.

Example:
Input: [(0, 0), (1, 1), (1, 2)]
Output: 2
It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2).
"""


def minSteps_2points(cur, next):
    # input: 2 tuples cur & next (x,y)
    # output: no. min steps to walk from cur to next
    x0, y0 = cur[0], cur[1]
    x1, y1 = next[0], next[1]
    delta_x = abs(x0 - x1)
    delta_y = abs(y0 - y1)
    return min([delta_x, delta_y]) + abs(
        delta_x - delta_y
    )  # min steps = diagonal + axis difference


def minSteps_sequence(points):
    # input: list points of tuples (x, y)
    # output: no. min steps to walk all the points in that order
    # trivial case
    if len(points) < 2:
        return 0
    # else
    step = 0  # no. min steps initialized
    for i in range(len(points) - 1):
        curPoint = points[i]
        nextPoint = points[i + 1]
        minStep = minSteps_2points(curPoint, nextPoint)
        step += minStep  # aggregate no. min steps
    return step


def minSteps_sequence_test(points):
    print(points, "~>", minSteps_sequence(points))


if __name__ == "__main__":
    minSteps_sequence_test([(0, 0), (1, 1), (1, 2)])  # return 2
    minSteps_sequence_test([(0, 0), (4, 2)])  # return 4
    minSteps_sequence_test([(0, 0)])  # return 0
