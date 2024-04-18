# -----------------------------
# Author: Tuan Nguyen
# Date created: 20200726
#!182.py
# -----------------------------
"""
A graph is minimally-connected if it is connected 
and there is no edge that can be removed while still leaving the graph connected. 
For example, any binary tree is minimally-connected.

Given an undirected graph, check if the graph is minimally-connected. 
You can choose to represent the graph as either an adjacency matrix or adjacency list.
"""


class UndirectedGraph:
    def __init__(self):
        self.nodes = list()
        self.edges = list()
        self.graph = dict()

    def add_edge(self, u, v):
        if (u, v) in self.edges:
            return
        self.add_node(u)
        self.add_node(v)
        self.edges.append((u, v))
        self.add_to_graph(u, v)

    def add_node(self, n):
        if n not in self.nodes:
            self.nodes.append(n)

    def add_to_graph(self, u, v):
        if u not in self.graph.keys():
            self.graph[u] = list()
        if v not in self.graph.keys():
            self.graph[v] = list()
        self.graph[u].append(v)
        self.graph[v].append(u)

    def get_connecting_edges(self, n):
        return [(u, v) for (u, v) in self.edges if u == n]

    def get_adjacent_nodes(self, n):
        if n not in self.graph.keys():
            return []
        return self.graph[n]


class UnionFind:
    def __init__(self):
        self.set = (
            dict()
        )  # {node_name: {"parent": node_parent, "rank": node_rank}}

    def make_set(self, n):
        if n in self.set.keys():
            return
        self.set[n] = {"parent": n, "rank": 0}

    def find(self, x):
        if x not in self.set.keys():
            return None
        while x != self.set[x]["parent"]:
            x = self.set[x]["parent"]
        return x

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        if self.set[root_x]["rank"] < self.set[root_y]["rank"]:
            root_x, root_y = root_y, root_x
        self.set[root_y]["parent"] = root_x
        if self.set[root_x]["rank"] == self.set[root_y]["rank"]:
            self.set[root_x]["rank"] += 1
        return


def kruskal(graph):
    minimal_spanning_tree_edges = list()
    S = UnionFind()
    for n in graph.nodes:
        S.make_set(n)
    E = sorted(graph.edges)
    for u, v in E:
        if S.find(u) != S.find(v):
            minimal_spanning_tree_edges.append((u, v))
            S.union(u, v)
    return minimal_spanning_tree_edges


def is_graph_minimally_connected(graph):
    original_edges = graph.edges
    minimal_spanning_tree_edges = kruskal(graph)
    if len(original_edges) == len(minimal_spanning_tree_edges):
        return True
    return False


def test1():
    G = UndirectedGraph()
    G.add_edge(1, 2)
    G.add_edge(1, 3)
    G.add_edge(2, 4)
    G.add_edge(2, 5)
    G.add_edge(3, 4)
    G.add_edge(4, 5)
    assert is_graph_minimally_connected(G) == False


def test2():
    G = UndirectedGraph()
    G.add_edge(1, 2)
    G.add_edge(1, 3)
    G.add_edge(2, 4)
    G.add_edge(2, 5)
    assert is_graph_minimally_connected(G) == True


if __name__ == "__main__":
    test1()
    test2()
