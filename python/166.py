# --------------------------
# Author: Tuan Nguyen
# Date created: 20191130
#!166.py
# --------------------------
"""
Implement a 2D iterator class. It will be initialized with an array of arrays, and should implement the following methods:

* next(): returns the next element in the array of arrays. If there are no more elements, raise an exception.
* has_next(): returns whether or not the iterator still has elements left.

For example, given the input [[1, 2], [3], [], [4, 5, 6]], calling next() repeatedly should output 1, 2, 3, 4, 5, 6.

Do not use flatten or otherwise clone the arrays. Some of the arrays can be empty.
"""


class Iterator:
    """ """

    def __init__(self, arr):
        """initialize Iterator object with an array of arrays"""
        self._arr = arr
        self._n = len(arr)  # no. sub-arrays
        self._row = 0  # initialize cursor at position (0,0)
        self._col = 0

    def next(self):
        """returns the next element in the array of arrays"""
        while (
            self._row < self._n and not self._arr[self._row]
        ):  # current sub-array is empty
            self._row += 1  # move to next sub-array
            self._col = 0
        if self._row >= self._n:
            raise ValueError("No element left")
        # else
        answer = self._arr[self._row][self._col]  # current element
        # update next cursor
        if (
            self._col == len(self._arr[self._row]) - 1
        ):  # end of current sub-array
            self._row += 1  # move to next sub-array
            self._col = 0
        else:
            self._col += 1  # else: move to next element in sub-array
        return answer

    def has_next(self):
        """returns whether or not the iterator still has elements left"""
        while (
            self._row < self._n and not self._arr[self._row]
        ):  # current sub-array is empty
            self._row += 1  # move to next sub-array
            self._col = 0
        if self._row >= self._n:  # end of master-array already
            return False
        return True


# ----- end of Iterator class -----


def test_iterator1():
    print("--- Test 1 ---")
    iterator = Iterator([[1, 2], [3], [], [4, 5, 6]])
    while iterator.has_next():
        print(iterator.next())


def test_iterator2():
    print("--- Test 2 ---")
    iterator = Iterator([[], [], []])
    while iterator.has_next():
        print(iterator.next())


def test_iterator3():
    print("--- Test 3 ---")
    iterator = Iterator([[], [1], [], [2], [3], []])
    while iterator.has_next():
        print(iterator.next())


if __name__ == "__main__":
    test_iterator1()  # expected: 1, 2, 3, 4, 5, 6 line-by-line
    test_iterator2()  # expected: blank
    test_iterator3()  # expected: 1, 2, 3 line-by-line
