"""
Invert a binary tree.

For example, given the following tree:

    a
   / \
  b   c
 / \  /
d   e f
should become:

  a
 / \
 c  b
 \  / \
  f e  d
"""

class BinaryTree:
    """ a linked-node-based implementation for binary tree """

    # ----- nested Node class -----
    class _Node:
        """ lightweight non-public structure for storing tree node """
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
        if n == self.left(parent):
            return self.right(parent)
        else:
            return self.left(parent)
    
    def children(self, n):
        """ return a generator for Node n's children """
        if self.left(n):
            yield self.left(n)
        if self.right(n):
            yield self.right(n)
        
    def num_children(self, n):
        """ return number of Node n's children """
        counter = 0
        if self.left(n):
            counter += 1
        if self.right(n):
            counter += 1
        return counter
    
    def is_root(self, n):
        """ return True if Node n is root of tree """
        return n == self._root
    
    def is_leaf(self, n):
        """ return True if Node n is leaf """
        return self.num_children(n) == 0

    # public update methods
    def add_root(self, e):
        """ add element e as root and return new Node """
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
    
    def invert(self):
        """ invert the current binary tree by preorder traversal """
        if not self.is_empty():
            self._subtree_invert(self.root())
    
    # non-public update methods
    def _subtree_invert(self, n):
        """ invert the subtree rooted at n by preorder traversal """
        n._left , n._right = n._right, n._left  # swap left child to right child and vice versa
        for c in self.children(n):
            self._subtree_invert(c)


def main():
    T = BinaryTree()
    r = T.add_root('a')
    lr = T.add_left(r, 'b')
    rr = T.add_right(r, 'c')
    llr = T.add_left(lr, 'd')
    rlr = T.add_right(lr, 'e')
    lrr = T.add_left(rr, 'f')

    assert T.left(T.root()).element() == 'b'
    T.invert()
    assert T.left(T.root()).element() == 'c'


if __name__ == "__main__":
    main()