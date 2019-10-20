# ----------------------------
# Author: Tuan Nguyen
# Date created: 20191020
#!solutions/135.py
# ----------------------------
"""
Given a binary tree, find a minimum path sum from root to a leaf.

For example, the minimum path in this tree is [10, 5, 1, -1], which has sum 15.

  10
 /  \
5    5
 \     \
   2    1
       /
     -1
"""

class BinaryTree:
    """ a linked-node-based implementation for binary tree """

    # ----- nested Node class -----
    class _Node:
        """ lightweight nonpublic structure for tree node """
        def __init__(self, e, p=None, l=None, r=None):
            self._element = e
            self._parent = p
            self._left = l
            self._right = r
            self._sum = 0   # store the path sum up till this node
        
        def element(self):
            return self._element
    # ----- end of nested Node class -----

    # BinaryTree methods
    def __init__(self):
        self._root = None
        self._size = 0
        self._sum_collection = []   # store path sums from root to all leaves

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
    
    def sibling(self, n):
        parent = self.parent(n)
        if parent is None:      # n is root
            return None
        if n == self.left(n):   # n is left child
            return self.right(n)
        else:                   # n is right child
            return self.left(n)
    
    def children(self, n):
        """ return a generator of Node n's children """
        if self.left(n):
            yield self.left(n)
        if self.right(n):
            yield self.right(n)
    
    def num_children(self, n):
        counter = 0
        if self.left(n):
            counter += 1
        if self.right(n):
            counter += 1
        return counter
    
    def is_root(self, n):
        return n == self._root
    
    def is_leaf(self, n):
        return self.num_children(n) == 0

    def min_path_sum(self):
        """ return minimum path sum from root to a leaf """
        if not self.is_empty():
            self._subtree_path_sum(self.root())
        return min(self._sum_collection)
    
    # non-public accessor
    def _subtree_path_sum(self, n):
        """ generate values for _sum_collection:
        calculate the path sums from root to all leaves """
        parent = self.parent(n)
        if parent is None:                      # n is root
            n._sum = n._element                 # root sum is root element
        else:                                   
            n._sum = parent._sum + n._element   # node sum = parent sum + node element
        if self.is_leaf(n):                     
            self._sum_collection.append(n._sum) # add leaf sum to sum collection
        else:       
            for c in self.children(n):          # else: find path sum of its children recursively
                self._subtree_path_sum(c)
    
    # public update methods
    def add_root(self, e):
        """ add e as root and return new Node """
        if self._root is not None:
            raise ValueError('Root exists')
        self._root = self._Node(e)
        self._size = 1
        return self._root
    
    def add_left(self, n, e):
        """ add e as left child of Node n and return new Node """
        if self.left(n) is not None:
            raise ValueError('Left child exists')
        newest = self._Node(e, n)
        n._left = newest
        self._size += 1
        return newest
    
    def add_right(self, n, e):
        """ add e as right child of Node n and return new Node """
        if self.right(n) is not None:
            raise ValueError('Right child exists')
        newest = self._Node(e, n)
        n._right = newest
        self._size += 1
        return newest


def main():
    T = BinaryTree()
    r = T.add_root(10)
    lr = T.add_left(r, 5)
    rr = T.add_right(r, 5)
    rlr = T.add_right(lr, 2)
    lrr = T.add_left(rr, 2)
    rrr = T.add_right(rr, 1)
    lrrr = T.add_left(rrr, -1)
    assert T.min_path_sum() == 15


if __name__ == "__main__":
    main()