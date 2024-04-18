"""
Given a list of points, a central point, and an integer k, find the nearest k points from the central point.

For example, given the list of points [(0, 0), (5, 4), (3, 1)], the central point (1, 2), and k = 2, return [(0, 0), (3, 1)].
"""

from operator import itemgetter


def kNearestPoints(points, central_point, k):
    # input: list of points (x, y), a central point (x_C, y_c) & int k
    # output: list of k nearest points from central point
    # trival cases
    if k <= 0:
        return []
    if k >= len(points):
        return points
    # else
    x_c = central_point[0]  # x-coordinate of central point
    y_c = central_point[1]  # y-coordinate of central point
    distance_list = (
        []
    )  # list of [point (x,y), distance to central point] initialized
    kList = []  # list of k nearest points initialized
    # compute distance from each points to central points, then push entry into distance_list
    for point in points:
        x = point[0]
        y = point[1]
        d = (x - x_c) ** 2 + (y - y_c) ** 2  # distance ^ 2
        distance_list.append([point, d])
    distance_list = sorted(
        distance_list, key=itemgetter(1)
    )  # sort distance_list ascendingly by distance
    # add k nearest points into kList
    for i in range(k):
        chosenPoint = distance_list[i][0]
        kList.append(chosenPoint)
    return kList


def kNearestPoints_test(points, central_point, k, desiredVal):
    print(kNearestPoints(points, central_point, k) == desiredVal)


if __name__ == "__main__":
    kNearestPoints_test(
        points=[(0, 0), (5, 4), (3, 1)],
        central_point=(1, 2),
        k=2,
        desiredVal=[(0, 0), (3, 1)],
    )
