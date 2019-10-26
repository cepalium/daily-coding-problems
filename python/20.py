# ---------------------------
# Author: Tuan Nguyen
# Date created: 20191026
#!20.py
# ---------------------------
"""
Given two singly linked lists that intersect at some point, 
find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, 
return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
"""

class SinglyLinkedList:
    """ an implementation for singly linked list """

    # ----- nested Node class -----
    class _Node:
        """ lightweight, nonpublic structure for stoing list node """
        def __init__(self, e, n):
            self._element = e
            self._next = n
        
        def element(self):
            return self._element
        
        def next(self):
            return self._next
    # ----- end of nested Node class -----

    # SinglyLinkedList methods
    def __init__(self):
        """ create an empty list """
        self._head = None
        self._tail = None
        self._size = 0

    # public accessors
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def head(self):
        """ return head node in list """
        if self.is_empty():
            return None
        return self._head
    
    def tail(self):
        """ return tail node in list """
        if self.is_empty():
            return None
        return self._tail
    
    # public update methods
    def add_first(self, e):
        """ add e as 1st node in list """
        newest = self._Node(e, self._head)
        self._head = newest
        if self.is_empty():
            self._tail = newest
        self._size += 1
    
    def add_last(self, e):
        """ add e as last node in list """
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def remove_first(self):
        """ remove 1st node in list & return the old 1st node's element """
        if self.is_empty():
            raise ValueError('List is empty')
        node = self._head
        self._head = self._head._next
        answer = node._element
        node._element, node._next = None, None  # help garbage collection
        self._size -= 1
        return answer
# ----- end of SinglyLinkedList class -----

def intersectingNode(L1, L2):
    """ return the intersecting node of 2 input singly linked list """
    size1 = len(L1)
    size2 = len(L2)
    nodeL1 = L1.head()
    nodeL2 = L2.head()
    if size1 > size2:
        for _ in range(size1 - size2):
            nodeL2 = nodeL2.next()
    elif size2 > size1:
        for _ in range(size2 - size1):
            nodeL1 = nodeL1.next()
    else:
        pass
    while nodeL1.element() is not None:
        if nodeL1.element() == nodeL2.element():
            return nodeL1
        else:
            nodeL1 = nodeL1.next()
            nodeL2 = nodeL2.next()
    return None

def test_intersectingNode():
    # create list A
    A = SinglyLinkedList()
    A.add_last(3)
    A.add_last(7)
    A.add_last(8)
    A.add_last(10)
    # create list B
    B = SinglyLinkedList()
    B.add_last(99)
    B.add_last(1)
    B.add_last(8)
    B.add_last(10)
    # find intersecting node of list A & B
    intersect = intersectingNode(A, B)
    # validate
    assert(intersect.element() == 8)

if __name__ == "__main__":
    test_intersectingNode()
