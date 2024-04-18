# ------------------------
# Author: Tuan Nguyen
# Date created: 20191020
#!solutions/117.py
# ------------------------
"""
Given a binary tree, return the level of the tree with minimum sum.
"""


class BinaryTree:
    """a linked-node-based implementation for binary tree"""

    # ----- nested Node class -----
    class _Node:
        """lightweight non-public structure for tree node"""

        def __init__(self, e, p=None, l=None, r=None):
            self._element = e
            self._parent = e
            self._left = l
            self._right = r

        def element(self):
            return self._element

    # ----- end of nested Node class -----

    # BinaryTree methods
    def __init__(self):
        """create an empty tree"""
        self._root = None
        self._size = 0

    # public accessors
    def __len__(self):
        """return number of nodes in tree"""
        return self._size

    def is_empty(self):
        """return True if tree is empty"""
        return self._size == 0

    def root(self):
        """return root node"""
        return self._root

    def parent(self, n):
        """return parent node of Node n"""
        return n._parent

    def left(self, n):
        """return left child of Node n"""
        return n._left

    def right(self, n):
        """return right child of Node n"""
        return n._right

    def sibling(self, n):
        """return sibling of Node n"""
        parent = self.parent(n)
        if parent is None:  # n is root
            return None
        if n == self.left(parent):  # n is left child
            return self.right(parent)
        else:  # n is right child
            return self.left(parent)

    def children(self, n):
        """return a generator of Node n's children"""
        if self.left(n):
            yield self.left(n)
        if self.right(n):
            yield self.right(n)

    def num_children(self, n):
        """return number of children of Node n"""
        counter = 0
        if self.left(n):
            counter += 1
        if self.right(n):
            counter += 1
        return counter

    def is_root(self, n):
        """return True if Node n is root"""
        return n == self._root

    def is_leaf(self, n):
        """return True if Node n is leaf"""
        return self.num_children(n) == 0

    def height(self, n=None):
        """return height of subtree rooted at Node n
        Root is at level 0"""
        if n is None:
            n = self.root()
        return self._height2(n)  # start height 2 recursion

    # non-public accessors
    def _height2(self, n):
        """return height of subtree rooted at Node n"""
        if self.is_leaf(n):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(n))

    # public update methods
    def add_root(self, e):
        """add e as root and return new Node"""
        if self._root is not None:
            raise ValueError("Root exists")
        self._root = self._Node(e)
        self._size = 1
        return self._root

    def add_left(self, n, e):
        """add e as left child of Node n and return new Node"""
        if self.left(n) is not None:
            raise ValueError("Left child exists")
        newest = self._Node(e, n)  # new node with n as parent
        n._left = newest
        self._size += 1
        return newest

    def add_right(self, n, e):
        """add e as right child of Node n and return new Node"""
        if self.right(n) is not None:
            raise ValueError("Right child exists")
        newest = self._Node(e, n)
        n._right = newest
        self._size += 1
        return newest


def main():
    T = BinaryTree()
    r = T.add_root(1)
    lr = T.add_left(r, 2)
    rr = T.add_right(r, 3)
    llr = T.add_left(lr, 4)
    rlr = T.add_right(lr, 5)
    lllr = T.add_left(llr, 6)
    assert T.height() == 3


if __name__ == "__main__":
    main()
