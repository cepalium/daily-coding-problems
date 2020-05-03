# ----------------------------
# Author: Tuan Nguyen
# Date created: 20200503
#!356.py
# ----------------------------
"""
Implement a queue using a set of fixed-length arrays.

The queue should support enqueue, dequeue, and get_size operations.
"""
class ArrayQueue:
    def __init__(self):
        self.capacity = 3
        self.data = [None for i in range(self.capacity)]
        self.head = -1
        self.tail = -1
        self.size = 0
    
    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size
    
    def first(self):
        if self.is_empty():
            return None
        return self.data[self.head]
    
    def last(self):
        if self.is_empty():
            return None
        return self.data[self.tail]
    
    def enqueue(self, e):
        if self.is_full():
            self.resize(2*self.capacity)
        self.tail = (self.tail + 1) % self.capacity
        self.data[self.tail] = e
        if self.is_empty():
            self.head = 0
        self.size += 1
    
    def is_full(self):
        return self.size == self.capacity
    
    def dequeue(self):
        if self.is_empty():
            return None
        item = self.data[self.head]
        self.data[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return item
    
    def resize(self, new_capacity):
        self.new_array = [None for i in range(new_capacity)]
        for i in range(self.capacity):
            self.new_array[i] = self.data[(self.head + i) % self.capacity]
        self.data = self.new_array.copy()
        self.head = 0
        self.tail = self.capacity - 1
        self.capacity = new_capacity



# ----- unit tests -----
def test_enqueue():
    q = ArrayQueue()
    q.enqueue(5)
    assert q.get_size() == 1
    assert q.first() == 5
    assert q.last() == 5

def test_dequeue():
    q = ArrayQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    a = q.dequeue()
    b = q.dequeue()
    assert a == 1
    assert b == 2
    assert q.get_size() == 1
    assert q.first() == 3
    assert q.last() == 3

def test_resize():
    q = ArrayQueue()
    assert q.capacity == 3
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    assert q.capacity == 6
    assert q.get_size() == 4
    assert q.first() == 1
    assert q.last() == 4

if __name__ == "__main__":
    test_enqueue()
    test_dequeue()
    test_resize()