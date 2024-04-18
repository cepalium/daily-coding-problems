# ------------------------------
# Author: Tuan Nguyen
# Date created: 20191015
#!solutions/154.py
# ------------------------------
"""
Implement a stack API using only a heap. A stack implements the following methods:

* push(item), which adds an element to the stack
* pop(), which removes and returns the most recently added element (or throws an error if there is nothing on the stack)

Recall that a heap has the following operations:

* push(item), which adds a new key to the heap
* pop(), which removes and returns the max value of the heap
"""


class HeapPriorityQueue:
    """a heap-based priority queue implementation"""

    # ----- nested Item class -----
    class _Item:
        """lightweright, non-public structure for storing heap node"""

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            """return True if self's key < other's key"""
            return self._key < other._key

    # ----- end of nested Item class -----

    # public behaviors of priority queue
    def __init__(self):
        """create an empty priority queue"""
        self._data = []

    def __len__(self):
        """return number of elements in pqueue"""
        return len(self._data)

    def is_empty(self):
        """return True if pqueue is empty"""
        return len(self._data) == 0

    def add(self, k, v):
        """add new (k,v) pair into pqueue"""
        newest = self._Item(k, v)
        self._data.append(newest)
        self._upheap(len(self._data) - 1)

    def min(self):
        """return, not remove, (k,v) pair of min pair in heap"""
        if self.is_empty():
            raise Exception("Priority queue is empty")
        item = self._data[0]
        return (item._key, item._value)

    def remove_min(self):
        """remove and return (k,v) pair of min pair in heap"""
        if self.is_empty():
            raise Exception("Priority queue is empty")
        self._swap(0, len(self._data) - 1)
        item = self._data.pop()
        self._downheap(0)  # fix heap from root
        return (item._key, item._value)

    # non-public behaviors of heap priority queue
    def _parent(self, j):
        """return index of j's parent"""
        return (j - 1) // 2

    def _left(self, j):
        """return index of j's left child"""
        return 2 * j + 1

    def _right(self, j):
        """return index of j's right child"""
        return 2 * j + 2

    def _has_left(self, j):
        """return True if j's left child exists"""
        return self._left(j) < len(self._data)

    def _has_right(self, j):
        """return True if j's right child exists"""
        return self._right(j) < len(self._data)

    def _swap(self, i, j):
        """swap the pair at indices i & j"""
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        """upheap the object at index j to correct heap properties"""
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)  # recur at porent's position

    def _downheap(self, j):
        """downheap object at index j to correct heap properties"""
        if self._has_left(j):
            left = self._left(j)
            small_child = left
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[small_child] < self._data[j]:
                self._swap(j, small_child)
                self._downheap(small_child)  # recur at small child's position


class HeapStack:
    """a stack using only a heap"""

    def __init__(self):
        self._heap = HeapPriorityQueue()
        self._sequenceNumber = (
            0  # act as key for (k,v) pair in heap priority queue
        )

    def push(self, item):
        """adds an element to the stack"""
        self._heap.add(self._sequenceNumber, item)
        self._sequenceNumber -= (
            1  # decrement the sequence number for the later-added item
        )

    def pop(self):
        """removes and returns the most recently added element"""
        if self._heap.is_empty():
            raise Exception("Stack is empty")
        item = self._heap.remove_min()
        answer = item[1]
        item = (None, None)  # help garbage collection
        return answer


def heapStack_test():
    S = HeapStack()
    S.push(1)
    S.push(2)
    S.push(3)
    print(S.pop() == 3)
    print(S.pop() == 2)
    print(S.pop() == 1)


if __name__ == "__main__":
    heapStack_test()
