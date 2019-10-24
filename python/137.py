# -----------------------------
# Author: Tuan Nguyen
# Date created: 20190928
#!solutions/137.py
# -----------------------------
"""
Implement a bit array.

A bit array is a space efficient array that holds a value of 1 or 0 at each index.

* init(size): initialize the array with size
* set(i, val): updates index at i with val where val is either 1 or 0.
* get(i): gets the value at index i.
"""

""" A bit array is a space efficient array that holds a value of 1 or 0 at each index. """
class BitArray:
    """ constructor """
    def __init__(self):
        self.data = list()
        self.size = 0

    """ initialize the array with size """
    def init(self, size):
        self.data = [0 for j in range(size)]
        self.size = size
    
    """ updates index at i with val where val is either 1 or 0 """
    def set(self, i, val):
        if i < 0 or i >= self.size:
            raise Exception("Invalid index: " + str(i))
        if val != 0 and val != 1:
            raise Exception("Invalid value: " + str(val))
        self.data[i] = val
    
    """ gets the value at index i """
    def get(self, i):
        if i < 0 or i >= self.size:
            raise Exception("Invalid index: " + str(i))
        return self.data[i]


def bitArray_test():
    bitArray = BitArray()
    bitArray.init(10)
    bitArray.set(1, 1)
    print(bitArray.get(1))


if __name__ == "__main__":
    bitArray_test()