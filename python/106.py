# --------------------------
# Author: Tuan Nguyen
# Date created: 20190827
#!solutions/106.py
# --------------------------
"""
Given an integer list where each number represents the number of hops you can make, 
determine whether you can reach to the last index starting at index 0.

For example, [2, 0, 1, 0] returns True while [1, 1, 0, 1] returns False.
"""


def isReachable(hops, source, dest):
    # input: list hops of int s.t each int is no. hops, int source position, int dest position
    # output: true if dest is reachable from source position
    visited = [False for i in range(len(hops))]  # array of visited index
    dest %= len(
        hops
    )  # make sure dest in [0, len(hops)-1], even negative input
    while not visited[source]:  # loop until the current index is not visited
        source %= len(hops)  # make sure source in [0, len(hops)-1]
        if hops[source] == 0 and source == dest:  # dest is reachable
            return True
        visited[source] = True  # update visited index
        source = source + hops[source]  # update next hop index
    return False  # reach this: dest in unreachable


def isHoppingToLast_test(hops):
    print("{}, 0~>last: {}".format(hops, isReachable(hops, 0, -1)))


if __name__ == "__main__":
    isHoppingToLast_test([2, 0, 1, 0])  # return True
    isHoppingToLast_test([1, 1, 0, 1])  # return False
