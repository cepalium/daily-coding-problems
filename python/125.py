# --------------------------
# Author: Tuan Nguyen
# Date created: 20191123
#!125.py
# --------------------------
"""
Given the root of a binary search tree, and a target K, return two nodes in the tree whose sum equals K.

For example, given the following tree and K of 20
    10
   /   \
 5      15
       /  \
     11    15
Return the nodes 5 and 15.
"""


class BinarySearchTree:
    class _Item:
        """(k,v) pair"""

        def __init__(self, k, v):
            self._key = k
            self._value = v

    # ----- end of Item class
    class Node:
        """BST node"""

        def __init__(self, e, p=None, l=None, r=None):
            self._element = e
            self._parent = p
            self._left = l
            self._right = r

        def element(self):
            return self._element

        def key(self):
            return self.element()._key

        def value(self):
            return self.element()._value

    # ----- end of Node class -----

    # fundamental
    def __init__(self):
        """create an empty BST"""
        self._root = None
        self._size = 0

    # public accessors
    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def root(self):
        return self._root

    def parent(self, n):
        return n._parent

    def left(self, n):
        return n._left

    def right(self, n):
        return n._right

    def children(self, n):
        if self.left(n) is not None:
            yield self.left(n)
        if self.right(n) is not None:
            yield self.right(n)

    # nonpublic accessors
    def _subtree_search(self, n, k):
        if k == n.key():
            return n
        else:
            if self.left(n) is not None and k < n.key():
                return self._subtree_search(self.left(n), k)
            if self.right(n) is not None and k > n.key():
                return self._subtree_search(self.right(n), k)
        return n  # unsuccessful search

    # public update methods
    def insert(self, k, v):
        item = self._Item(k, v)
        if self.is_empty():
            leaf = self._add_root(item)
        else:
            n = self._subtree_search(self.root(), k)
            if k == n.key():
                n.element()._value = v
                leaf = n
            elif k < n.key():
                leaf = self._add_left(n, item)
            else:
                leaf = self._add_right(n, item)
        return leaf

    # nonpublic update methods
    def _add_root(self, item):
        self._root = self.Node(item)
        self._size = 1
        return self._root

    def _add_left(self, n, item):
        newest = self.Node(item, n)
        n._left = newest
        self._size += 1
        return newest

    def _add_right(self, n, item):
        newest = self.Node(item, n)
        n._right = newest
        self._size += 1
        return newest

    # extend
    def two_nodes_sum_to_K(self, K):
        if len(self) < 2:
            raise ValueError("Tree has less than 2 nodes")
        visited = 0
        n1, n2 = self._subtree_two_nodes_sum_to_K(self.root(), K, visited)
        return n1, n2

    def _subtree_two_nodes_sum_to_K(self, n, k, visited):
        visited += 1
        if visited == self._size:
            return self.root(), self.root()  # fail to find 2 nodes
        m = self._subtree_search(self.root(), k - n.key())
        if m.key() == k - n.key() and m != n:  # found 2 valid nodes
            return n, m
        else:
            for c in self.children(n):
                return self._subtree_two_nodes_sum_to_K(c, k, visited)


# ----- end of BST class -----


def test_two_nodes_sum_to_K():
    bst = BinarySearchTree()
    n10 = bst.insert(10, 10)
    n5 = bst.insert(5, 5)
    n15 = bst.insert(15, 15)
    n11 = bst.insert(11, 11)

    # test 1
    nK1, nK2 = bst.two_nodes_sum_to_K(K=20)
    assert nK1.key() == 5
    assert nK2.key() == 15
    # test 2
    nK1, nK2 = bst.two_nodes_sum_to_K(K=21)
    assert nK1.key() == 10
    assert nK2.key() == 11


if __name__ == "__main__":
    test_two_nodes_sum_to_K()
