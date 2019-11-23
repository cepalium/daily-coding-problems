# --------------------------
# Author: Tuan Nguyen
# Date created: 20191123
#!89.py
# --------------------------
"""
Determine whether a tree is a valid binary search tree.

A binary search tree is a tree with two children, left and right, 
and satisfies the constraint that the key in the left child must be less than or equal to the root 
and the key in the right child must be greater than or equal to the root.
"""
class BinarySearchTree:

    class _Item:
        """ (k,v) pair """
        def __init__(self, k, v):
            self._key = k
            self._value = v
    # ----- end of Item class
    class Node:
        """ BST node """
        def __init__(self, e, p=None, l=None, r=None):
            self._element = e   # Item object
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
        """ create an empty BST """
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

    def first(self):
        return self._subtree_first_node(self.root()) if not self.is_empty() else None
    
    def last(self):
        return self._subtree_last_node(self.root()) if not self.is_empty() else None
    
    def before(self, n):
        if self.left(n) is not None:
            return self._subtree_last_node(self.left(n))
        else:
            walk = n
            above = self.parent(walk)
            while above is not None and walk == self.left(above):
                walk = above
                above = self.parent(walk)
            return above
    
    def after(self, n):
        if self.right(n) is not None:
            return self._subtree_first_node(self.right(n))
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
        return n    # unsuccessful search
    
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
    def is_valid(self):
        """ return True if BST is valid """
        if self.is_empty():
            return True
        valid_flag = True
        self._subtree_is_valid(self.root(), valid_flag)
        return valid_flag
    
    def _subtree_is_valid(self, n, flag):
        """ generate True/False flag for each subtree rooted at n """
        left, right = self.left(n), self.right(n)
        if left is not None and left.key() > n.key():
            flag &= False
        if right is not None and right.key() < n.key():
            flag &= False
        if left is not None:
            self._subtree_is_valid(left, flag)
        if right is not None:
            self._subtree_is_valid(right, flag)
# ----- end of BST class -----

def test_validate_BST():
    bst = BinarySearchTree()
    bst.insert(10, 10)
    bst.insert(6, 6)
    bst.insert(12, 12)
    assert bst.is_valid() == True

if __name__ == "__main__":
    test_validate_BST()