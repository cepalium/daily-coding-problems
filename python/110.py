# --------------------------
# Author: Tuan Nguyen

"""
Given a binary tree, return all paths from the root to leaves.

For example, given the tree:
   1
  / \
 2   3
    / \
   4   5
Return [[1, 2], [1, 3, 4], [1, 3, 5]].
"""


class BinaryTree:
    """a linked-node-based implementation for binary tree"""

    # ----- nested Node class -----
    class _Node:
        """non-public structure for storing tree node"""

        def __init__(self, e, p=None, l=None, r=None):
            self._element = e
            self._parent = p
            self._left = l
            self._right = r
            self._path = (
                []
            )  # list of nodes indicating the path from root to this node

    # ----- end of nested Node class -----

    # BinaryTree methods
    def __init__(self):
        """create an empty tree"""
        self._root = None
        self._size = 0
        self._path_collection = []  # store all paths from root to leaves

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
        if parent is None:  # n is root
            return None
        if n == self.left(parent):  # n is left child
            return self.right(parent)
        else:  # n is right child
            return self.left(parent)

    def children(self, n):
        """return a generator for Node n's children"""
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

    def paths_to_all_leaves(self):
        """return all paths from the root to leaves"""
        if not self.is_empty():
            self._subtree_paths_to_all_leaves(
                self.root()
            )  # build tree's path collection from root
        return self._path_collection

    # non-public accessors
    def _subtree_paths_to_all_leaves(self, n):
        """return all paths for subtree rooted at n by preorder traversal"""
        parent = self.parent(n)
        if parent is None:  # n is root
            path = [n._element]  # path to root has only root element
        else:
            path = [i for i in parent._path]  # parent path
            path.append(n._element)  # child path = parent path + child element
        n._path = path  # save child path to its node
        if self.is_leaf(n):  # if n is leaf
            self._path_collection.append(
                n._path
            )  # add its path to tree's path collection
        else:  # else, recur on its children
            for c in self.children(n):
                self._subtree_paths_to_all_leaves(c)

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
        newest = self._Node(e, n)
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
    lrr = T.add_left(rr, 4)
    rrr = T.add_right(rr, 5)
    assert T.paths_to_all_leaves() == [[1, 2], [1, 3, 4], [1, 3, 5]]


if __name__ == "__main__":
    main()
