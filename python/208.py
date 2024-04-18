# -------------------------------
# Author: Tuan Nguyen
# Date created: 20191207
#!208.py
# -------------------------------
"""
Given a linked list of numbers and a pivot k, 
partition the linked list so that all nodes less than k come before nodes greater than or equal to k.

For example, given the linked list 5 -> 1 -> 8 -> 0 -> 3 and k = 3, 
the solution could be 1 -> 0 -> 5 -> 8 -> 3.
"""


class SinglyLinkedList:
    """singly linked list data structure"""

    class _Node:
        """node structure"""

        def __init__(self, e, n):
            self._element = e
            self._next = n

        def element(self):
            return self._element

        def next(self):
            return self._next

    # ----- end of Node class -----

    def __init__(self):
        """create an empty list"""
        self._head = self._Node(None, None)
        self._tail = self._Node(None, None)
        self._size = 0

    # public accessors
    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def head(self):
        """return head node"""
        if self.is_empty():
            return None
        return self._head

    def tail(self):
        """return tail node"""
        if self.is_empty():
            return None
        return self._tail

    def print_list(self):
        """print all elements from list in-line"""
        node = self.head()
        while node is not None:
            print(node.element(), end=" ")
            node = node.next()
        print()

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
        self._tail._next = newest
        self._tail = newest
        if self.is_empty():
            self._head = newest
        self._size += 1

    def remove_first(self):
        """remove 1st node in list & return its element"""
        if self.is_empty():
            return None
        answer = self._head.element()
        self._head = self._head.next()
        self._size -= 1
        if self._size == 0:
            self._tail = self._Node(None, None)
        return answer


# ----- end of SinglyLinkedList node -----


def partitioned_linked_list(L, k):
    """return a linked list which all nodes in L less than k come before nodes greater than or equal to k"""
    L_partitioned = SinglyLinkedList()
    node = L.head()
    while node is not None:  # traverse list from head node
        if node.element() < k:
            L_partitioned.add_first(
                node.element()
            )  # nodes less than k come before
        else:
            L_partitioned.add_last(
                node.element()
            )  # nodes greater than or equal to k come after
        node = node.next()
    return L_partitioned


def test_partitioned_linked_list():
    L = SinglyLinkedList()
    L.add_last(5)
    L.add_last(1)
    L.add_last(8)
    L.add_last(0)
    L.add_last(3)
    L.print_list()  # expected: 5 1 8 0 3

    L_partitioned = partitioned_linked_list(L, k=3)
    L_partitioned.print_list()  # expected: 0 1 5 8 3


if __name__ == "__main__":
    test_partitioned_linked_list()
