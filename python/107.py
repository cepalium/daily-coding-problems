# ------------------------
# Author: Tuan Nguyen
# Date created: 20191020
#!solutions/107.py
# -----------------------
"""
Print the nodes in a binary tree level-wise. 
For example, the following should print 1, 2, 3, 4, 5.
  1
 / \
2   3
   / \
  4   5
"""


class BinaryTree:
    """a linked-node-based implementation for binary tree"""

    # ----- nested Node class -----
    class _Node:
        """lightweight non-public structure for storing tree node"""

        def __init__(self, e, p=None, l=None, r=None):
            self._element = e
            self._parent = p
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
        """return parent of Node n"""
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
        if n == self.left(parent):
            return self.right(parent)
        else:
            return self.left(parent)

    def children(self, n):
        """return a generator of Node n's children"""
        if self.left(n):
            yield self.left(n)
        if self.right(n):
            yield self.right(n)

    def num_children(self, n):
        """return number of Node n's children"""
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

    def print_level_wise(self):
        """print the nodes in tree level-wise"""
        breadfirst_lst = []
        fringe = []
        fringe.append(self.root())
        while fringe:
            n = fringe.pop(0)
            breadfirst_lst.append(n.element())
            for c in self.children(n):
                fringe.append(c)
        print(", ".join(str(i) for i in breadfirst_lst))

    # public update methods
    def add_root(self, e):
        """add element e as root and return new Node"""
        if self._root is not None:
            raise ValueError("Root exists")
        self._root = self._Node(e)
        self._size = 1
        return self._root

    def add_left(self, n, e):
        """add element e as left chilf of Node n and return new Node"""
        if self.left(n) is not None:
            raise ValueError("Left child exists")
        newest = self._Node(e, n)  # new node with n as parent
        n._left = newest
        self._size += 1
        return newest

    def add_right(self, n, e):
        """add element e as right child of Node n and return new Node"""
        if self.right(n) is not None:
            raise ValueError("Right child exists")
        newest = self._Node(e, n)  # new node with n as parent
        n._right = newest
        self._size += 1
        return newest


def main():
    T = BinaryTree()
    r = T.add_root(1)
    lr = T.add_left(r, 2)
    rr = T.add_right(r, 3)
    lrr = T.add_left(rr, 4)
    rrr = T.add_right(rr, 5)
    T.print_level_wise()


if __name__ == "__main__":
    main()
