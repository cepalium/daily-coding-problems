# -----------------------------
# Author: Tuan Nguyen
# Date created: 20200322
#!314.py
# -----------------------------
"""
You are the technical director of WSPT radio, serving listeners nationwide. 
For simplicity's sake we can consider each listener to live along a horizontal line stretching from 0 (west) to 1000 (east).

Given a list of N listeners, and a list of M radio towers, each placed at various locations along this line, 
determine what the minimum broadcast range would have to be in order for each listener's home to be covered.

For example, suppose listeners = [1, 5, 11, 20], and towers = [4, 8, 15]. 
In this case the minimum range would be 5, since that would be required for the tower at position 15 to reach the listener at position 20.
"""


def min_broadcast_range(listeners, towers):
    """return the min range s.t towers will cover all listeners"""
    # trivial cases
    if len(listeners) == 0:
        return 0
    if len(towers) == 0:
        return None
    ranges = []  # store the distance of each listener to the nearest tower
    for listener in listeners:
        nearest_tower_dist = abs(listener - towers[0])
        for tower in towers[1:]:
            if abs(listener - tower) < nearest_tower_dist:
                nearest_tower_dist = abs(listener - tower)
            elif abs(listener - tower) == nearest_tower_dist:
                pass
            else:  # greater
                break
        ranges.append(nearest_tower_dist)
    return max(
        ranges
    )  # max distance from all nearest-to-tower distances is the min required broadcast range


def test1():
    assert (
        min_broadcast_range(listeners=[1, 5, 11, 20], towers=[4, 8, 15]) == 5
    )


def test2():
    assert min_broadcast_range(listeners=[1, 5, 11, 20], towers=[4, 8]) == 12


def test3():
    assert min_broadcast_range(listeners=[1, 5, 11, 20], towers=[8]) == 12


if __name__ == "__main__":
    test1()
    test2()
    test3()
