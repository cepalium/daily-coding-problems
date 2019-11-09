# ---------------------------
# Author: Tuan Nguyen
# Date created: 20191109
#!180.py
# ---------------------------
"""
Given a stack of N elements, interleave the first half of the stack with the second half reversed using only one other queue. 
This should be done in-place.

Recall that you can only push or pop from a stack, and enqueue or dequeue from a queue.

For example, if the stack is [1, 2, 3, 4, 5], it should become [1, 5, 2, 4, 3]. 
If the stack is [1, 2, 3, 4], it should become [1, 4, 2, 3].

Hint: Try working backwards from the end state.
"""

class Stack:
    """ adapter from Python3's list data structure """
    def __init__(self):
        self._data = []
    
    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def print(self):
        print(self._data)
    
    def push(self, e):
        self._data.append(e)
    
    def pop(self):
        return self._data.pop()
# ----- end of Stack class -----

class Queue:
    """ adapter from Python3's list data structure """
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data) == 0
    
    def print(self):
        print(self._data)

    def enqueue(self, e):
        self._data.append(e)

    def dequeue(self):
        return self._data.pop(0)
# ----- end of Queue class -----

def interleave_stack(stack: Stack()):
    """ interleave the first half of the stack with the second half reversed using only one other queue """
    queue = Queue()
    n = len(stack)
    for i in range(n):
        while len(stack) > i + 1:
            queue.enqueue(stack.pop())
        while not queue.is_empty():
            stack.push(queue.dequeue())


def interleavedStack_test1():
    stack = Stack()
    for i in range(1, 6):
        stack.push(i)
    stack.print()           # 1,2,3,4,5
    interleave_stack(stack)
    stack.print()           # 1,5,2,4,3


def interleavedStack_test2():
    stack = Stack()
    for i in range(1, 5):
        stack.push(i)
    stack.print()           # 1,2,3,4
    interleave_stack(stack)
    stack.print()           # 1,4,2,3


if __name__ == "__main__":
    interleavedStack_test1()
    interleavedStack_test2()