# --------------------------
# Author: Tuan Nguyen
# Date created: 20191123
#!133.py
# --------------------------
"""
Given a node in a binary search tree, return the next bigger element, also known as the inorder successor.

For example, the inorder successor of 22 is 30.

   10
  /  \
 5    30
     /  \
   22    35
You can assume each node has a parent pointer.
"""


class BinarySearchTree:
    class _Item:
        """(k,v) pair"""

        def __init__(self, k, v):
            self._key = k
            self._value = v

    # ----- end of Item class -----
    class Node:
        """BST node"""

        def __init__(self, e, p=None, l=None, r=None):
            self._element = e  # Item object
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

    def before(self, n):
        if self.left(n) is not None:
            return self.left(n)
        else:
            walk = n
            above = self.parent(walk)
            while above is not None and walk == self.left(above):
                walk = above
                above = self.parent(walk)
            return above

    def after(self, n):
        if self.right(n) is not None:
            return self.right(n)
        else:
            walk = n
            above = self.parent(walk)
            while above is not None and walk == self.right(above):
                walk = above
                above = self.parent(walk)
            return above

    # nonpublic accessors
    def _subtree_first_node(self, n):
        walk = n
        while self.left(walk) is not None:
            walk = self.left(walk)
        return walk

    def _subtree_last_node(self, n):
        walk = n
        while self.right(walk) is not None:
            walk = self.right(walk)
        return walk

    def _subtree_search(self, n, k):
        if k == n.key():
            return n
        else:
            if k < n.key() and self.left(n) is not None:
                return self._subtree_search(self.left(n), k)
            if k > n.key() and self.right(n) is not None:
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


# ----- end of BST class -----


def test_next_bigger():
    bst = BinarySearchTree()
    n10 = bst.insert(10, 10)
    n5 = bst.insert(5, 5)
    n30 = bst.insert(30, 30)
    n22 = bst.insert(22, 22)
    n35 = bst.insert(35, 35)
    assert bst.after(n22).key() == 30


if __name__ == "__main__":
    test_next_bigger()
