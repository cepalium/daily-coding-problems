# -----------------------------
# Author: Tuan Nguyen
# Date created: 20200512
#!365.py
# -----------------------------
"""
A quack is a data structure combining properties of both stacks and queues. 
It can be viewed as a list of elements written left to right such that three operations are possible:

* push(x): add a new item x to the left end of the list
* pop(): remove and return the item on the left end of the list
* pull(): remove the item on the right end of the list.

Implement a quack using three stacks and O(1) additional memory, 
so that the amortized time for any push, pop, or pull operation is O(1).
"""
class Quack:
    def __init__(self):
        """ create empty quack with empty 3 stacks; 
        aim to initialize new quack or reset 3 stacks when size = 0 """
        self.push_stack = []
        self.duplicate_push_stack = []
        self.pop_stack = []
        self._size = 0
    
    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0
    
    def push(self, x):
        self.push_stack.append(x)
        self.duplicate_push_stack.append(x)
        self._size += 1
    
    def pull(self):
        if self.is_empty():
            self.__init__()
            return None
        left_end_item = self.push_stack.pop(-1)
        self._size -= 1
        return left_end_item
    
    def pop(self):
        if self.is_empty():
            self.__init__()
            return None
        if not self.pop_stack:
            self._pour_elements_from_duplicate_push_stack_to_pop_stack()
        right_end_item = self.pop_stack.pop(-1)
        self._size -= 1
        return right_end_item
    
    def _pour_elements_from_duplicate_push_stack_to_pop_stack(self):
        while self.duplicate_push_stack:
            last_item_in_duplicate_push_stack = self.duplicate_push_stack.pop(-1)
            self.pop_stack.append(last_item_in_duplicate_push_stack)


def test1():
    quack = Quack()
    quack.push(1)
    quack.push(2)
    quack.push(3)
    assert quack.size() == 3
    assert quack.pop() == 1
    assert quack.pull() == 3
    assert quack.pull() == 2
    assert quack.size() == 0

if __name__ == "__main__":
    test1()
