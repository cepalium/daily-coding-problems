# ---------------------------
# Author: Tuan Nguyen
# Date created: 20200207
#!270.py
# ---------------------------
"""
A network consists of nodes labeled 0 to N. You are given a list of edges (a, b, t), 
describing the time t it takes for a message to be sent from node a to node b. 
Whenever a node receives a message, it immediately passes the message on to a neighboring node, if possible.

Assuming all nodes are connected, determine how long it will take for every node to receive a message that begins at node 0.

For example, given N = 5, and the following edges:
edges = [
    (0, 1, 5),
    (0, 2, 3),
    (0, 5, 4),
    (1, 3, 8),
    (2, 3, 1),
    (3, 5, 10),
    (3, 4, 5)
]

You should return 9, because propagating the message from 0 -> 2 -> 3 -> 4 will take that much time.
"""


def propagation_time(N, edges):
    """return the time taken for every node to receive a message from node 0"""
    shortest_time = -1  # output
    propagate_dict = {
        i: [-1, -1] for i in range(N + 1)
    }  # dict { node i: [shortest time for msg from node 0 to reach node i, predecessor] }
    propagate_dict[0] = [0, -1]  # initialize at node 0
    # propagation
    for edge in edges:
        a, b, t = edge[0], edge[1], edge[2]
        (t_a, t_b,) = (
            propagate_dict[a][0],
            propagate_dict[b][0],
        )
        if (
            t_b == -1 or t_b > t_a + t
        ):  # node b isn't reached yet or reach time at node b isn't optimal
            propagate_dict[b] = [t_a + t, a]
    # find the time when all nodes receive the msg
    for node_i, item_i in propagate_dict.items():
        reach_time = item_i[0]
        if reach_time > shortest_time:
            shortest_time = reach_time
    return shortest_time


def test_1():
    N = 5
    edges = [
        (0, 1, 5),
        (0, 2, 3),
        (0, 5, 4),
        (1, 3, 8),
        (2, 3, 1),
        (3, 5, 10),
        (3, 4, 5),
    ]
    assert propagation_time(N=N, edges=edges) == 9


if __name__ == "__main__":
    test_1()
