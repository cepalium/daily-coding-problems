# ------------------------------
# Author: Tuan Nguyen
# Date created: 20191123
#!112.py
# ------------------------------
"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree. 
Assume that each node in the tree also has a pointer to its parent.

According to the definition of LCA on Wikipedia: 
“The lowest common ancestor is defined between two nodes v and w as the lowest node in T 
that has both v and w as descendants (where we allow a node to be a descendant of itself).”
"""


class BinaryTree:
    class Node:
        """binary tree node"""

        def __init__(self, e, p=None, l=None, r=None):
            self._element = e
            self._parent = p
            self._left = l
            self._right = r

        def element(self):
            return self._element

    # ----- end of Node class -----

    # fundamental
    def __init__(self):
        """create an empty binary tree"""
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

    def depth(self, n):
        """return the depth of node n in tree. Root has depth 0"""
        if n == self.root():
            return 0
        else:
            return 1 + self.depth(self.parent(n))

    # public update methods
    def add_root(self, e):
        if self.root() is not None:
            raise ValueError("Root exists")
        self._root = self.Node(e)
        self._size = 1
        return self._root

    def add_left(self, n, e):
        if self.left(n) is not None:
            raise ValueError("Left child exists")
        newest = self.Node(e, n)
        n._left = newest
        self._size += 1
        return newest

    def add_right(self, n, e):
        if self.right(n) is not None:
            raise ValueError("Right child exists")
        newest = self.Node(e, n)
        n._right = newest
        self._size += 1
        return newest

    # extend
    def lca(self, a, b):
        """return the lowest common ancestor (LCA) node of 2 nodes a & b"""
        d_a, d_b = self.depth(a), self.depth(b)  # depth
        w_a, w_b = a, b  # walk
        # adjust to a & b's ancestors at same depth
        while d_a > d_b:
            w_a = self.parent(w_a)
            d_a -= 1
        while d_b > d_a:
            w_b = self.parent(w_b)
            d_b -= 1
        # find lowest common ancestor from this depth
        while d_a > 0:
            if w_a == w_b:  # find common ancestor of a and b at same depth
                return w_a
            else:  # move up 1 level of ancestor for both a & b
                w_a = self.parent(w_a)
                w_b = self.parent(w_b)
        return self.root()  # lca is root at depth 0


# ----- end of BinaryTree class -----


def test_lca():
    T = BinaryTree()
    r = T.add_root(10)
    lr = T.add_left(r, 5)
    rr = T.add_right(r, 15)
    lrr = T.add_left(rr, 11)
    assert T.lca(rr, lrr).element() == 15
    assert T.lca(lr, rr).element() == 10


if __name__ == "__main__":
    test_lca()
