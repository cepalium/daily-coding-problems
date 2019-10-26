"""
Implement a stack that has the following methods:

* push(val), which pushes an element onto the stack
* pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
* max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.

Each method should run in constant time.
"""

class Stack:
    """ a linked-node implementation for stack """

    # ----- nested Node class -----
    class _Node:
        """ lightweight, nonpublic structure for storing stack node """
        def __init__(self, e, n):
            self._element = e
            self._next = n
            self._max = None
    # ----- end of nested Node class -----

    # Stack methods
    def __init__(self):
        self._top = None
        self._size = 0
    
    # public accessors
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def pop(self):
        """ remove and return the topmost element in stack """
        if self.is_empty():
            return None
        return self._remove_first()

    def max(self):
        """ return, not remove, the currently max element in stack """
        return self._top._max
    
    # public update method
    def push(self, val):
        """ push val into stack """
        self._add_first(val)
    
    # private update method
    def _add_first(self, e):
        """ add eleemnt e to top of stack """
        newest = self._Node(e, self._top)
        if self.is_empty():
            curMax = None
        else:
            curMax = self._top._max
        self._top = newest
        # update top
        self._top = newest
        # update current max of stack at top node
        self._top._max = e if (curMax is None) or (e > curMax) else prevMax
        # update size
        self._size += 1
    
    def _remove_first(self):
        """ remove and return the last element in stack """
        node = self._top
        self._top = self._top._next
        self._size -= 1
        answer = node._element
        node._element, node._next = None, None  # help garbage collection
        return answer
# ----- end of Stack class -----

def test_stack():
    stack = Stack()
    stack.push(1)               # stack {1}
    assert stack.max() == 1
    stack.push(2)               # stack {2,1}
    stack.push(3)               # stack {3,2,1}
    assert stack.max() == 3
    pop = stack.pop()           # stack {2,1}
    assert pop == 3
    assert stack.max() == 2
    stack.pop()                 # stack {1}
    stack.pop()                 # stack {}
    assert stack.is_empty() == True

if __name__ == "__main__":
    test_stack()