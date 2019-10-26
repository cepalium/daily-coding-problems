"""
Given a singly linked list and an integer k, 
remove the kth last element from the list. 
k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.
"""

class Node:
    """ lightweight nonpublic structure for storing list node """
    def __init__(self, e, n):
        self.element = e
        self.next = n

# ----- end of  Node class -----

class SinglyLinkedList:
    """ an implemenation of singly linked list """
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    
    # public accessors
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def head(self):
        if self.is_empty():
            return None
        return self._head
    
    def last(self):
        if self.is_empty():
            return None
        return self._tail
    
    def printList(self):
        node = self._head
        while node is not None:
            print(node.element, end=' ')
            node = node.next
        print("")
    
    # public update methods
    def add_first(self, e):
        newest = Node(e, self._head)
        if self.is_empty():
            self._tail = newest
        self._head = newest
        self._size += 1
    
    def add_last(self, e):
        newest = Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail.next = newest
        self._tail = newest
        self._size += 1

    def remove_first(self):
        if self.is_empty():
            return None
        node = self._head
        self._head = self._head.next
        self._size -= 1
        if self._size == 0:
            self._tail = None
        answer = node.element
        node.element, node.next = None, None
        return answer
# ----- end of nested Node class -----

def remove_kth_node(L, k):
    """ remove and return the kth last element from the list 
    k=0: last element
    k=1: second last element 
    k = n-1: first element """
    n = len(L)
    if k < 0 or k >= n:
        raise ValueError('Invalid k: ' + k)
    if k == n-1:    
        return L.remove_first()
    cur = L.head()
    prev = L.head()
    for i in range(n-k):
        if i == n-k-1:
            successor = cur.next
            prev.next = successor
            item = cur.element
            cur.element, cur.next = None, None
            return item
        prev = cur
        cur = cur.next
    return None


def test_remove():
    L = SinglyLinkedList()
    L.add_last(1)
    L.add_last(2)
    L.add_last(3)
    L.add_last(4)
    L.add_last(5)
    L.printList()

    remove_kth_node(L, 3)

    L.printList()


if __name__ == "__main__":
    test_remove()