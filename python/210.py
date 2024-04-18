# -------------------------------
# Author: Tuan Nguyen
# Date created: 20191209
#!210.py
# -------------------------------
"""
A Collatz sequence in mathematics can be defined as follows. Starting with any positive integer:

* If n is even, the next number in the sequence is n / 2
* If n is odd, the next number in the sequence is 3n + 1 

It is conjectured that every such sequence eventually reaches the number 1. Test this conjecture.
Bonus: What input n <= 1000000 gives the longest sequence?
"""


class CollatzSequence:
    """class for Collatz sequence"""

    def __init__(self, start):
        """constructor"""
        self._sequence_list = list()
        self._start = start

    # public accessors
    def to_int(self):
        """return Collatz sequence as concatenated integer"""
        if self._is_empty():
            self._generate_collatz_sequence()
        str_collatz_sequence = "".join(str(i) for i in self._sequence_list)
        return int(str_collatz_sequence)

    def to_list(self):
        """return Collatz sequence as list of numbers"""
        if self._is_empty():
            self._generate_collatz_sequence()
        return self._sequence_list

    def num_steps(self):
        """return number of steps from start number to reach 1"""
        if self._is_empty():
            self._generate_collatz_sequence()
        return (
            len(self._sequence_list) - 1
        )  # exclude 1st element, i.e start number

    # non-public methods
    def _is_empty(self):
        return len(self._sequence_list) == 0

    def _generate_collatz_sequence(self):
        """generate collatz sequence from start number"""
        n = self._start
        while n != 1:
            self._sequence_list.append(int(n))
            if n % 2 == 0:  # even number
                n = n // 2
            else:  # odd number
                n = 3 * n + 1
        self._sequence_list.append(int(n))  # add 1 as last number


# ----- end of CollatzSequence class -----


def collatz_max_n(max_num, include_max=False):
    """return max n < max_num s.t it has the most steps to reach 1 in Collatz sequence"""
    max_steps = -1
    max_n = -1
    if include_max:
        max_num += 1
    for i in range(1, max_num):
        collatz = CollatzSequence(start=i)
        num_steps = collatz.num_steps()
        if num_steps > max_steps:
            max_steps = num_steps
            max_n = i
    return max_n


# TESTs
def test_conjecture():
    """test if every Collatz sequence eventually reaches the number 1"""
    for i in range(1, 10000):
        collatz = CollatzSequence(start=i)
        collatz_int = collatz.to_int()
        assert collatz_int % 10 == 1
    print("Conjecture test: PASSED")


def test_collatz_max_n():
    """test if implementation returns the correct number with most steps until reaching 1 by Collatz sequence definition"""
    # test 1
    print(collatz_max_n(max_num=10, include_max=False))
    assert collatz_max_n(max_num=10, include_max=False) == 9
    # test 2
    print(collatz_max_n(max_num=100, include_max=False))
    assert collatz_max_n(max_num=100, include_max=False) == 97
    # test 3
    print(collatz_max_n(max_num=1000, include_max=False))
    assert collatz_max_n(max_num=1000, include_max=False) == 871
    # test 4
    print(collatz_max_n(max_num=10000, include_max=False))
    assert collatz_max_n(max_num=10000, include_max=False) == 6171


if __name__ == "__main__":
    test_conjecture()
    test_collatz_max_n()
