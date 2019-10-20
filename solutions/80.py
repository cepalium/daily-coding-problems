# -------------------------
# Author: Tuan Nguyen
# Date created: 20191020
#!solutions/80.py
# -------------------------
"""
Given the root of a binary tree, return a deepest node. 
For example, in the following tree, return d.
    a
   / \
  b   c
 /
d
"""

class BinaryTree:
    """ a linked-list-based implementation for binary tree """

    # ----- nested Node class -----
    class _Node:
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
        """ create an empty tree """
        self._root = None
        self._size = 0

    # public accessors
    def __len__(self):
        """ return number of nodes in tree """
        return self._size
    
    def is_empty(self):
        """ return True if tree is empty """
        return self._size == 0

    def root(self):
        """ return root node """
        return self._root
    
    def parent(self, n):
        """ return parent node of Node n """
        if self.is_root(n):
            return None
        return n._parent
    
    def left(self, n):
        """ return left child of Node n """
        return n._left
    
    def right(self, n):
        """ return right child of Node n """
        return n._right
    
    def sibling(self, n):
        """ return sibling of Node n """
        parent = self.parent(n)
        if n == self.left(parent):      # n is left child
            return self.right(parent)   # return right child
        else:
            return self.left(parent)    # else return left child
    
    def children(self, n):
        """ return a generator of Node's n children """
        if self.left(n) is not None:
            yield self.left(n)
        if self.right(n) is not None:
            yield self.right(n)
    
    def num_children(self, n):
        """ return number of Node n's children """
        counter = 0
        if self.left(n) is not None:
            counter += 1
        if self.right(n) is not None:
            counter += 1
        return counter
    
    def is_root(self, n):
        """ return True if Node n is root """
        return n == self._root
    
    def is_leaf(self, n):
        """ return True if Node n is leaf """
        return self.num_children(n) == 0
    
    def deepestNode(self):
        """ return deepest node's element by breadfirst traversal """
        if self.is_empty():     # empty tree
            return None
        else:                   # tree has at least 1 node
            fringe = []
            deepest = None
            fringe.append(self.root())  # start with root
            while fringe:
                n = fringe.pop(0)   # first node in fringe
                for c in self.children(n):  # enqueue with n's children
                    fringe.append(c)
                if not fringe:      # n is the last node in queue
                    deepest = n     # deepest node is n
            return deepest
    
    # public update methods
    def add_root(self, e):
        """ add element e as root and return new Node """
        if self._root is not None:
            raise ValueError('Root exists')
        self._root = self._Node(e)
        self._size = 1
        return self._root
    
    def add_left(self, n, e):
        """ add element e as left child of Node n and return new Node """
        if self.left(n):
            raise ValueError('Left child exists')
        newest = self._Node(e, n)
        n._left = newest
        self._size += 1
        return newest
    
    def add_right(self, n, e):
        """ add eleemnt e as right child of Node n and return new Node """
        if self.right(n):
            raise ValueError('Right child exists')
        newest = self._Node(e, n)
        n._right = newest
        self._size += 1
        return newest


def main():
    T = BinaryTree()
    r = T.add_root('a')
    lr = T.add_left(r, 'b')
    rr = T.add_right(r, 'c')
    llr = T.add_left(lr, 'd')
    assert T.deepestNode().element() == 'd'


if __name__ == "__main__":
    main()