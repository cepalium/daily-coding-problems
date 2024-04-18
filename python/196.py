# -----------------------------
# Author: Tuan Nguyen
# Date created: 20191126
#!196.py
# -----------------------------
"""
Given the root of a binary tree, find the most frequent subtree sum. 
The subtree sum of a node is the sum of all values under a node, including the node itself.

For example, given the following tree:
```
  5
 / \
2  -5
```
Return 2 as it occurs twice: once as the left leaf, and once as the sum of 2 + 5 - 5.
"""


class BinaryTree:
    class Node:
        """binary tree node"""

        def __init__(self, e, p=None, l=None, r=None):
            self._element = e
            self._parent = p
            self._left = l
            self._right = r
            self._sum = e  # initial subtree sum at this node

    # ----- end of Node class -----

    # fundamental
    def __init__(self):
        """create an empty tree"""
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
    def most_frequent_subtree_sum(self):
        """return the most frequent subtree sum"""
        sum_freq = dict()  # dictionary of frequencies of each subtree sum
        self._subtree_sum(
            self.root(), sum_freq
        )  # generate result for sum_freq, start from root
        return max(
            sum_freq, key=lambda k: sum_freq[k]
        )  # return most common subtree sum

    # non-public accessors
    def _subtree_sum(self, n, sum_freq):
        """calculate subtree sum by post-order traversal"""
        for c in self.children(n):
            self._subtree_sum(c, sum_freq)
        # post-order operations
        # current node's sum
        child_sum = n._sum
        # update this node's parent sum
        parent = self.parent(n)
        if parent is not None:
            parent._sum += child_sum
        # update sum frequency dict
        sum_freq[child_sum] = (
            1 if child_sum not in sum_freq.keys() else sum_freq[child_sum] + 1
        )


# ----- end of BinaryTree class


def test_most_frequent_subtree_sum():
    T = BinaryTree()
    r = T.add_root(5)
    lr = T.add_left(r, 2)
    rr = T.add_right(r, -5)
    assert T.most_frequent_subtree_sum() == 2


if __name__ == "__main__":
    test_most_frequent_subtree_sum()
