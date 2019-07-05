# ---------------------------------------
# Author: Tuan Nguyen
# Date: 20190705
#!solutions/53.py
# ---------------------------------------
"""
Implement a queue using two stacks. 
Recall that a queue is a FIFO (first-in, first-out) data structure with the following methods: 
enqueue, which inserts an element into the queue, and dequeue, which removes it.
"""

"""
Implementation of a queue using 2 stacks
Behavior: FIFO
Methods:
* enqueue(x): insert x into queue
* dequeue(): remove 1st element of queue
"""
class QueueFrom2Stacks():
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    

    def __repr__(self):
        return "{0}".format(self.stack1)


    def enqueue(self, x):
    # insert x into queue
        self.stack1.append(x)
    

    def dequeue(self):
    # remove the 1st element in queue
        while self.stack1:  # push elements in stack1 from last into stack2, i.e 1st element in queue is last element in stack2
            li = self.stack1.pop()
            self.stack2.append(li)
        fo = self.stack2.pop()  # 1st element in queue is last element in stack2
        while self.stack2:  # push elements in stack2 from last into stack1, i.e 1st element in queue is 1st element in stack1
            fi = self.stack2.pop()
            self.stack1.append(fi)
        return fo


def main():
    queue = QueueFrom2Stacks()  # init object from class QueueFrom2Stacks()
    queue.enqueue(1)    # insert 1 into queue
    queue.enqueue(2)    # insert 2 into queue
    queue.enqueue(3)    # insert 3 into queue
    print(queue)    # [1, 2, 3]
    queue.dequeue() # remove 1st element in queue, i.e 1
    print(queue)    # [2, 3]
    queue.dequeue() # remove 1st element in queue, i.e 2
    print(queue)    # [3]


if __name__ == "__main__":
    main()        