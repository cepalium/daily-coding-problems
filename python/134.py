# ----------------------------
# Author: Tuan Nguyen
# Date created: 20190928
#!solutions/134.py
# ----------------------------
"""
You have a large array with most of the elements as zero.

Use a more space-efficient data structure, SparseArray, that implements the same interface:

* init(arr, size): initialize with the original large array and size.
* set(i, val): updates index at i with val.
* get(i): gets the value at index i.
"""


class SparseArray:
    """constructor"""

    def __init__(self):
        self.data = (
            dict()
        )  # use map data structure as spare array {index: val}
        self.size = 0

    """ initialize with the original large array and size """

    def init(self, arr, size):
        self.data = {
            i: arr[i] for i in range(len(arr)) if arr[i] != 0
        }  # input SparseArray by input arr, skip index with zero-value
        self.size = size

    """ updates index at i with val """

    def set(self, i, val):
        if i < 0 or i >= self.size:
            raise Exception("Invalid index: " + str(i))
        self.data[i] = val

    """ gets the value at index i """

    def get(self, i):
        if i < 0 or i >= self.size:
            raise Exception("Invalid index: " + str(i))
        if i in self.data.keys():
            return self.data[i]
        else:
            return 0


def sparseArray_test():
    a = [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        2,
        5,
        0,
        0,
        2,
        5,
        0,
        5,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        5,
        5,
        0,
        5,
        4,
        0,
        7,
        5,
        0,
        0,
        4,
        79,
        4,
        0,
        2,
        1,
    ]
    sparseA = SparseArray()
    sparseA.init(a, len(a))
    print(sparseA.data)
    print(sparseA.get(24))
    sparseA.set(24, 10)
    print(sparseA.get(24))


if __name__ == "__main__":
    sparseArray_test()
