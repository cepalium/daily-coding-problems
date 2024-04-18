"""
Let's represent an integer in a linked list format by having each node represent a digit in the number. 
The nodes make up the number in reversed order.

For example, the following linked list:

1 -> 2 -> 3 -> 4 -> 5

is the number 54321.

Given two linked lists in this format, return their sum in the same linked list format.

For example, given

9 -> 9
5 -> 2
return 124 (99 + 25) as:

4 -> 2 -> 1
"""


class Node:
    """lightweight, nonpublic structure for stoing list node"""

    def __init__(self, e, n):
        self._element = e
        self._next = n

    def element(self):
        return self._element

    def next(self):
        return self._next


# ----- end of nested Node class -----


class SinglyLinkedList:
    """an implementation for singly linked list"""

    # SinglyLinkedList methods
    def __init__(self):
        """create an empty list"""
        self._head = None
        self._tail = None
        self._size = 0

    # public accessors
    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def head(self):
        """return head node in list"""
        if self.is_empty():
            return None
        return self._head

    def tail(self):
        """return tail node in list"""
        if self.is_empty():
            return None
        return self._tail

    def printList(self):
        node = self._head
        while node is not None:
            print(node._element, end=" ")
            node = node._next
        print("")

    # public update methods
    def add_first(self, e):
        """add e as 1st node in list"""
        newest = Node(e, self._head)
        self._head = newest
        if self.is_empty():
            self._tail = newest
        self._size += 1

    def add_last(self, e):
        """add e as last node in list"""
        newest = Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def remove_first(self):
        """remove 1st node in list & return the old 1st node's element"""
        if self.is_empty():
            raise ValueError("List is empty")
        node = self._head
        self._head = self._head._next
        answer = node._element
        node._element, node._next = None, None  # help garbage collection
        self._size -= 1
        return answer


# ----- end of SinglyLinkedList class -----


def sum_linked_list(L1, L2):
    L = SinglyLinkedList()
    # construct numbers from 2 lists
    node1 = L1.head()
    node2 = L2.head()
    number1, multiplier1 = 0, 1
    number2, multiplier2 = 0, 1
    while node1 is not None:
        number1 += node1.element() * multiplier1  # reversed-order list
        node1 = node1.next()
        multiplier1 *= 10
    while node2 is not None:
        number2 += node2.element() * multiplier2  # reversed-order list
        node2 = node2.next()
        multiplier2 *= 10
    # construct the sum linked list
    sum_number = number1 + number2
    while sum_number != 0:
        d = sum_number % 10  # last digit in sum_number
        L.add_last(d)  # add digit to list in reversed order
        sum_number //= (
            10  # next sum_number is quotient from current sum_number & 10
        )
    return L


def test_sum():
    A = SinglyLinkedList()
    A.add_last(9)
    A.add_last(9)

    B = SinglyLinkedList()
    B.add_last(5)
    B.add_last(2)

    C = sum_linked_list(A, B)
    C.printList()


if __name__ == "__main__":
    test_sum()
