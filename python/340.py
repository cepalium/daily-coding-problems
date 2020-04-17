# --------------------------
# Author: Tuan Nguyen
# Date created: 20200417
#!340.py
# --------------------------
"""
Given a set of points (x, y) on a 2D cartesian plane, find the two closest points. 
For example, given the points [(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)], return [(-1, -1), (1, 1)].
"""
def two_closest_points(points):
    """ return a pair of 2 closest points (in list) """
    n = len(points)
    if n < 2:  # trivial cases
        return []
    if n == 2:
        return points
    min_dist = compute_distance(points[0], points[1])  # initial conditions
    closest_pair = [points[0], points[1]]
    for i in range(n-1):
        for j in range(i+1, n):
            a, b = points[i], points[j]
            dist_ab = compute_distance(a, b)
            if dist_ab < min_dist:
                closest_pair = [a, b]
                min_dist = dist_ab
    return closest_pair

def compute_distance(point_a, point_b):
    """ return the squared distance from point_a to point_b """
    x_a, y_a = point_a[0], point_a[1]
    x_b, y_b = point_b[0], point_b[1]
    return (x_a - x_b)**2 + (y_a - y_b)**2

def test():
    assert two_closest_points([(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)]) == [(1, 1), (-1, -1)]

if __name__ == "__main__":
    test()