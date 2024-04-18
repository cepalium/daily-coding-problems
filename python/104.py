# -----------------------
# Author: Tuan Nguyen
# Date created: 20191026
#!104.py
# -----------------------
"""
Determine whether a doubly linked list is a palindrome. 
What if it’s singly linked?

For example, 1 -> 4 -> 3 -> 4 -> 1 returns True while 1 -> 4 returns False.
"""


class DoublyLinkedList:
    """imlementation for doubly linked list"""

    # ----- nested Node class -----
    class _Node:
        """lightweight, nonpublic structure for list node"""

        def __init__(self, e, p, n):
            self._element = e
            self._prev = p
            self._next = n

        def element(self):
            return self._element

        def prev(self):
            return self._prev

        def next(self):
            return self._next

    # ----- end of nested Node class -----

    # DoublyLinkedList methods
    def __init__(self):
        """create an empty list"""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    # public accessors
    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def head(self):
        """return 1st node in list"""
        if self.is_empty():
            return None
        return self._header._next

    def last(self):
        """return last node in list"""
        if self.is_empty():
            return None
        return self._trailer._prev

    # public update methods
    def add_first(self, e):
        self._add_between(e, self._header, self._header._next)

    def add_last(self, e):
        self._add_between(e, self._trailer._prev, self._trailer)

    def remove_first(self):
        return self._remove(self._header._next)

    def remove_last(self):
        return self._remove(self._trailer._prev)

    # private update methods
    def _add_between(self, e, p, n):
        newest = self._Node(e, p, n)
        p._next = newest
        n._prev = newest
        self._size += 1

    def _remove(self, n):
        """remove Node n and return n's element"""
        predecessor = n._prev
        successor = n._next
        predecessor._next = successor  # update predecessor & successor
        successor._prev = predecessor
        answer = n._element
        n._element, n._prev, n._next = (
            None,
            None,
            None,
        )  # help garbage collection
        self._size -= 1
        return answer


# ----- end of DoublyLinkedList class -----


def is_palindrome_linked_list(L):
    """return True if doubly linked list L is palindrome"""
    left = L.head()  # current node in left side
    right = L.last()  # current node in right side
    n = len(L)
    for _ in range(n // 2):  # iterate until middle node
        if (
            left.element() != right.element()
        ):  # left node is not mirrored to right node
            return False  # then list is not palindrome
        left = left.next()  # move to next nodes
        right = right.prev()
    return True  # reach this ~> list is palindrome


def test_palindromeList():
    # test 1
    A = DoublyLinkedList()
    A.add_last(1)
    A.add_last(4)
    A.add_last(3)
    A.add_last(4)
    A.add_last(1)
    assert is_palindrome_linked_list(A) == True
    # test 2
    B = DoublyLinkedList()
    B.add_last(1)
    B.add_last(4)
    assert is_palindrome_linked_list(B) == False


if __name__ == "__main__":
    test_palindromeList()
