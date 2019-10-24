# --------------------------
# Author: Tuan Nguyen
# Date created: 20191020
#!solutions/78.py
# --------------------------
"""
Given k sorted singly linked lists, write a function to merge all the lists into one sorted singly linked list.
"""

class SinglyLinkedList:
    """ an implememtation of singly linked list """

    # ----- nested Node class -----
    class _Node:
        """ lightweight non-public structure for storing linked list node """
        def __init__(self, e, n=None):
            self._element = e
            self._next = n
    # ----- end of nested Node class -----

    # Linked List methods
    def __init__(self):
        """ create an empty linked list """
        self._head = None
        self._tail = None
        self._size = 0

    # public accessors
    def __len__(self):
        """ return number of nodes in linked list """
        return self._size
    
    def is_empty(self):
        """ return True if list is empty """
        return self._size == 0
    
    def first(self):
        """ return, not remove, first element in list """
        if self.is_empty():
            return None
        return self._head._element
    
    def last(self):
        """ return, not remove, last element in list """
        if self.is_empty():
            return None
        return self._tail._element

    def printList(self):
        n = self._head
        s = str(n._element)
        while n._next:
            n = n._next
            s += ' -> ' + str(n._element)
        print(s)
    
    # public update methods
    def add_first(self, e):
        """ add element e to first of list """
        newest = self._Node(e, self._head)
        self._head = newest
        if self.is_empty():
            self._tail = self._head
        self._size += 1

    def add_last(self, e):
        """ add element e to last of list """
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def remove_first(self, e):
        """ remove and return the element in first node in list """
        if self.is_empty():
            raise ValueError('List is empty')
        n = self._head
        self._head = n._next
        self._size -= 1
        if self._size == 0:
            self._tail = None
        answer = n._element
        n._element, n._next = None, None
        return answer


def mergeAllSortedLists(lst_L):
    """ return 1 sorted singly linked list from list of k sorted singly linked list """
    if len(lst_L) <= 1:     # input list has 0/1 linked list
        return lst_L[0]
    # divide & recur
    L1 = mergeAllSortedLists(lst_L[:len(lst_L)//2])
    L2 = mergeAllSortedLists(lst_L[len(lst_L)//2:])
    # combine
    L3 = merge(L1, L2)
    return L3


def merge(A, B):
    """ """
    C = SinglyLinkedList()      # initialize output sorted linked list
    nA = A._head                # current node in A
    nB = B._head                # current node in B
    # ascendingly add element in A & B into C until 1 list is exhausted
    while nA and nB:
        if nA._element <= nB._element:
            C.add_last(nA._element)
            nA = nA._next
        else:
            C.add_last(nB._element)
            nB = nB._next
    # copy the rest of the other list into C
    while nA:
        C.add_last(nA._element)
        nA = nA._next
    while nB:
        C. add_last(nB._element)
        nB = nB._next
    return C


def main():
    L1 = SinglyLinkedList()
    L1.add_last(1)
    L1.add_last(2)
    L1.printList()

    L2 = SinglyLinkedList()
    L2.add_last(3)
    L2.add_last(4)
    L2.printList()

    L3 = SinglyLinkedList()
    L3.add_last(5)
    L3.add_last(6)
    L3.printList()

    Lk = mergeAllSortedLists([L1, L2, L3])
    Lk.printList()


if __name__ == "__main__":
    main()
