# ------------------------
# Author: Tuan Nguyen
# Date created: 20191105
#!177.py
# ------------------------
"""
Given a linked list and a positive integer k, rotate the list to the right by k places.

For example, given the linked list 7 -> 7 -> 3 -> 5 and k = 2, it should become 3 -> 5 -> 7 -> 7.

Given the linked list 1 -> 2 -> 3 -> 4 -> 5 and k = 2, it should become 3 -> 4 -> 5 -> 1 -> 2.
"""


class CircularLinkedList:
    """an implementation of circular linked list"""

    # ----- nested Node class -----
    class _Node:
        """lightweight, nonpublic structure for storing linked list node"""

        def __init__(self, e, n):
            self._element = e
            self._next = n

    # ----- end of nested Node class ------

    # CircularLinkedList methods
    def __init__(self):
        """create an empty linked list"""
        self._tail = None
        self._size = 0

    # public accessors
    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            return None
        return self._tail._next._element

    def last(self):
        if self.is_empty():
            return None
        return self._tail._element

    def print_list(self):
        """print all elements in line"""
        cur = self._tail._next
        for _ in range(self._size):
            print(cur._element, end=" ")
            cur = cur._next
        print()

    # public update methods
    def add_first(self, e):
        """add e as 1st in list"""
        if self.is_empty():
            self._tail = self._Node(e, None)
            self._tail._next = self._tail
        else:
            newest = self._Node(e, self._tail._next)
            self._tail._next = newest
        self._size += 1

    def add_last(self, e):
        """add e as last in list"""
        if self.is_empty():
            self._tail = self._Node(e, None)
            self._tail._next = self._tail
        else:
            newest = self._Node(e, self._tail._next)
            self._tail._next = newest
        self._tail = self._tail._next
        self._size += 1

    def remove_first(self):
        """remove and return the 1st element in list"""
        node = self._tail._next
        new_head = node._next
        self._tail._next = new_head
        answer = node._element
        node._element, node._next = None, None  # help garbage collection
        self._size -= 1
        return answer

    def rotate(self, k):
        """rotate the linked list k times"""
        if self.is_empty():
            raise ValueError("List is empty")
        if k < 0:
            raise ValueError("Invalid k:", k)
        for _ in range(k):
            self._tail = self._tail._next


def test1():
    print("=== TEST 1 ===")
    L = CircularLinkedList()
    L.add_last(7)
    L.add_last(7)
    L.add_last(3)
    L.add_last(5)
    L.print_list()  # 7, 7, 3, 5

    L.rotate(2)

    L.print_list()  # 3, 5, 7, 7


def test2():
    print("=== TEST 2 ===")
    L = CircularLinkedList()
    L.add_last(1)
    L.add_last(2)
    L.add_last(3)
    L.add_last(4)
    L.add_last(5)
    L.print_list()  # 1, 2, 3, 4, 5

    L.rotate(2)

    L.print_list()  # 3, 4, 5, 1, 2


if __name__ == "__main__":
    test1()
    test2()
