# -----------------------------
# Author: Tuan Nguyen
# Date created: 20191003
#!solutions/141.py
# -----------------------------
"""
Implement 3 stacks using a single list:

class Stack:
    def __init__(self):
        self.list = []

    def pop(self, stack_number):
        pass

    def push(self, item, stack_number):
        pass
"""

""" a list-based implementation of 3 stacks in 1 list"""
class Stack:
    """ constructor """
    def __init__(self):
        # default size of each stack 1, 2 & 3 initialized
        self.size1 = 1000
        self.size2 = 1000
        self.size3 = 1000
        # start index of each stack 1, 2 & 3 initialized
        self.mark1 = 0
        self.mark2 = self.size1
        self.mark3 = self.size1 + self.size2
        # top index of each stack 1, 2 & 3 initialized
        self.top1 = -1
        self.top2 = -1
        self.top3 = -1
        # 3 stacks in 1 list initialized
        self.list = [None for i in range(self.size1 + self.size2 + self.size3)]
    
    """ pop the last eleement of selected stack """
    def pop(self, stack_number):
        # error checking
        if stack_number < 0 or stack_number > 2:                    # invalid stack number
            raise IOError("Invalid stack: " + str(stack_number))
        if stack_number == 0 and self.top1 < 0:            # empty stack 1
            raise Exception("Empty stack 1")
        if stack_number == 1 and self.top2 < 0:            # empty stack 2
            raise Exception("Empty stack 2")
        if stack_number == 2 and self.top3 < 0:            # empty stack 3
            raise Exception("Empty stack 3")
        # pop
        if stack_number == 0:
            answer = self.list[self.top1 + self.mark1]
            self.list[self.top1 + self.mark1] = None
            self.top1 -= 1
        elif stack_number == 1:
            answer = self.list[self.top2 + self.mark2]
            self.list[self.top2 + self.mark2] = None
            self.top2 -= 1
        else:
            answer = self.list[self.top3 + self.mark3]
            self.list[self.top3 + self.mark3] = None
            self.top3 -= 1
        return answer

    """ push item into selected stack """
    def push(self, item, stack_number):
        # error checking
        if stack_number < 0 or stack_number > 2:
            raise IOError("Invalid stack: " + str(stack_number))
        # resize stack if full 
        if stack_number == 0 and self.top1 + self.mark1 + 1 == self.size1:
            self.resize(0, self.size1*2)
        if stack_number == 1 and self.top2 + self.mark2 + 1 == self.size1 + self.size2:
            self.resize(1, self.size2*2)
        if stack_number == 2 and self.top3 + self.mark3 + 1 == self.size1 + self.size2 + self.size3:
            self.resize(2, self.size3*2)
        # push
        if stack_number == 0:
            self.top1 += 1
            self.list[self.top1 + self.mark1] = item
        elif stack_number == 1:
            self.top2 += 1
            self.list[self.top2 + self.mark2] = item
        else:
            self.top3 += 1
            self.list[self.top3 + self.mark3] = item
        
    """ resize stack if full """
    def resize(self, stack_number, capacity):
        if stack_number == 0:
            self.resize1(capacity)
        elif stack_number == 1:
            self.resize2(capacity)
        else:
            self.resize3(capacity)

    """ """
    def resize1(self, capacity):
        for j in range(self.size1, capacity):
            self.list.insert(j, None)
        self.mark2 += capacity - self.size1     # shift the start index of stack2
        self.mark3 += capacity - self.size1     # shift the start index of stack3
        self.size1 = capacity                   # update the new capacity of stack1

    """ """
    def resize2(self, capacity):
        for j in range(self.size1+ self.size2, self.size1 + capacity):
            self.list.insert(j, None)
        self.mark3 += capacity - self.size2     # shift the start index of stack3
        self.size2 = capacity                   # update the new capacity of stack1

    """ """
    def resize3(self, capacity):
        for j in range(capacity - self.size3):
            self.list.push(None)
        self.size3 = capacity


def stack_test():
    stack = Stack()
    stack.push(1, 0)
    stack.push(5, 1)
    stack.push(10, 2)
    print(stack.pop(0))
    print(stack.pop(1))
    print(stack.pop(2))
    print(stack.pop(0))


if __name__ == "__main__":
    stack_test()
