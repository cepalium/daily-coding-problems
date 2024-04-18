# --------------------------
# Author: Tuan Nguyen
# Date created: 20191020
#!solutions/145.py
# --------------------------
"""
Given the head of a singly linked list, swap every two nodes and return its head.

For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3.
"""


class SinglyLinkedList:
    """an implemenation for singly linked list"""

    # ----- nested Node class -----
    class _Node:
        """lightweight non-public structure for storing list node"""

        def __init__(self, e, n):
            self._element = e
            self._next = n

    # ----- end of nested Node class -----

    # SinglylLinkedList methods
    def __init__(self):
        """create an empty list"""
        self._head = None
        self._tail = None
        self._size = 0

    # public accessors
    def __len__(self):
        """return number of nodes in list"""
        return self._size

    def is_empty(self):
        """return True if list is empty"""
        return self._size == 0

    def first(self):
        """return, not remove, first element in list"""
        if self.is_empty():
            raise ValueError("List is empty")
        return self._head._element

    def last(self):
        """return, not remove, last element in list"""
        if self.is_empty():
            raise ValueError("List is empty")
        return self._tail._element

    def print_list(self):
        n = self._head
        lst = []
        while n:
            lst.append(n._element)
            n = n._next
        print(" -> ".join(str(i) for i in lst))

    # public update methods
    def add_first(self, e):
        """add element e to first of list"""
        newest = self._Node(e, self._head)
        self._head = newest
        if self.is_empty():
            self._tail = newest
        self._size += 1

    def add_last(self, e):
        """add element e to last of list"""
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def remove_first(self):
        """remove and return the first element in list"""
        n = self._head
        answer = n._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        n._element, n._next = None, None
        return answer

    def swap(self):
        """given the head of a singly linked list, swap every 2 nodes and return its head"""
        n = self._head
        while n:
            after_n = n._next
            if after_n:
                n._element, after_n._element = (
                    after_n._element,
                    n._element,
                )  # swap element of Node n and its next Node
            n = after_n._next  # next n is jump 2 next positions
        return self._head._element


def main():
    L = SinglyLinkedList()
    L.add_last(1)
    L.add_last(2)
    L.add_last(3)
    L.add_last(4)

    print("Before swap:\t", end=" ")
    L.print_list()
    print("Head = ", L.first())

    print(L.swap())

    print("After swap:\t", end=" ")
    L.print_list()
    print("Head = ", L.first())


if __name__ == "__main__":
    main()
