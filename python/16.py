# ----------------------------
# Author: Tuan Nguyen
# Date: 20190529
#! 16.py
# ----------------------------
"""
You run an e-commerce website and want to record the last N order ids in a log. 

Implement a data structure to accomplish this, with the following API:
record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.

You should be as efficient with time and space as possible.
"""

class Order():
    def __init__(self):
        self.orderIds = []  # log w/ data structure := list, i.e queue
    
    
    def record(self, order_id):
    # input: int order_id
    # output: add order_id to the log
        self.orderIds.append(order_id)
    

    def get_last(self, i):
    # input: int i
    # output: i-th last element from the log
        return self.orderIds[len(self.orderIds) - 1 - i]


if __name__ == "__main__":
    eCommerceOrders = Order()
    # add order ids
    for i in range(1, 101):     # add log from 1 to 100
        eCommerceOrders.record(i)
    
    print(eCommerceOrders.get_last(10))     # return 90
    print(eCommerceOrders.get_last(50))     # return 50
