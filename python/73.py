# --------------------------
# Author: Tuan Nguyen
# Date created: 20191026
#!73.py
# --------------------------
"""
Given the head of a singly linked list, reverse it in-place.
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
    
    def printList(self):
        node = self._head
        while node is not None:
            print(node._element, end=' ')
            node = node._next
        print("")
    
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
    
    def reverse(self):
        cur, prev, nex = self._head, self._head, self._head
        while cur is not None:
            nex = cur._next     # save next node before reverse
            cur._next = prev if cur is not self._head else None
            if prev == self._head:
                self._tail = prev
            prev = cur
            cur = nex
        self._head = prev
# ----- end of SinglyLinkedList class -----

def test_reverse():
    L = SinglyLinkedList()
    L.add_last(1)
    L.add_last(2)
    L.add_last(3)
    L.printList()

    L.reverse()
    L.printList()


if __name__ == "__main__":
    test_reverse()