# -----------------------------
# Author: Tuan Nguyen
# Date created: 20200726
#!218.py
# -----------------------------
"""
Write an algorithm that computes the reversal of a directed graph. 
For example, if a graph consists of A -> B -> C, it should become A <- B <- C.
"""
class DirectedGraph:
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
        self.graph[u].append(v)

def reverse_directed_graph(graph):
    reversal_graph = DirectedGraph()
    for (u, v) in graph.edges:
        reversal_graph.add_edge(v, u)
    return reversal_graph


def test1():
    G = DirectedGraph()
    G.add_edge("A", "B")
    G.add_edge("B", "C")
    assert G.edges == [("A", "B"), ("B", "C")]
    reversed_G = reverse_directed_graph(G)
    assert reversed_G.edges == [("B", "A"), ("C", "B")]

if __name__ == "__main__":
    test1()