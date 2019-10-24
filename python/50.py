# -------------------------
# Author: Tuan Nguyen
# Date created: 20191020
#!solutions/50.py
# -------------------------
"""
Suppose an arithmetic expression is given as a binary tree. 
Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:
    *
   / \
  +    +
 / \  / \
3  2  4  5

You should return 45, as it is (3 + 2) * (4 + 5).
"""

class ArithmeticBinaryTree:
    """ a linked-list-based implemenation of Binary Tree """

    # ----- nested Node class -----
    class _Node:
        """ lightweight non-public structure for storing a tree node """
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
        """ create an empty binary tree """
        self._root = None
        self._size = 0
        self._expression = ""

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
        """ return left child node of Node n """
        return n._left
    
    def right(self, n):
        """ return right child node of Node n """
        return n._right
    
    def sibling(self, n):
        """ return sibling node of Node n """
        parent = self.parent(n)
        if n == self.left(parent):
            return self.right(parent)
        else:
            return self.left(parent)
    
    def children(self, n):
        """ generate an iteration of Node n's children """
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
        """ return True is Node n is leaf """
        return self.num_children(n) == 0

    def evaluate(self):
        """ return the result from arithmetic expression by inorder traversal """
        self.arithmeticInorder()
        return eval(self._expression)

    # public update methods
    def add_root(self, e):
        """ add element e as root node and return new node """
        if self.root() is not None:
            raise ValueError('Root exists')
        self._root = self._Node(e)
        self._size = 1
        return self._root
    
    def add_left(self, n, e):
        """ add element e as left child of Node n and return new node """
        if self.left(n) is not None:
            raise ValueError('Left child exists')
        newest = self._Node(e, n)   # n as parent node
        n._left = newest
        self._size += 1
        return newest
    
    def add_right(self, n, e):
        """ add element e as right child of Node n and return new node """
        if self.right(n) is not None:
            raise ValueError('Right child exists')
        newest = self._Node(e, n)   # n as parent node
        n._right = newest
        self._size += 1
        return newest
    
    # public arithmetic traversal method
    def arithmeticInorder(self, n=None):
        """ generate arithmetic expression from tree """
        if n is None:
            n = self.root()
        if not self.is_empty():
            self._subtree_arithmeticInorder(n)  # start from root
    
    # non-public arithmetic traveral method
    def _subtree_arithmeticInorder(self, n):
        """ generate arithmetic expression from subtree rooted at n """
        self._expression += "("

        if self.left(n) is not None:
            self._subtree_arithmeticInorder(self.left(n))
        
        self._expression += n._element

        if self.right(n) is not None:
            self._subtree_arithmeticInorder(self.right(n))

        self._expression += ")"


def main():
    T = ArithmeticBinaryTree()
    r = T.add_root('*')
    lr = T.add_left(r, '+')
    rr = T.add_right(r, '+')
    llr = T.add_left(lr, '3')
    rlr = T.add_right(lr, '2')
    lrr = T.add_left(rr, '4')
    rrr = T.add_right(rr, '5')
    assert T.evaluate() == 45


if __name__ == "__main__":
    main()        