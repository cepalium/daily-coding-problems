# ----------------------------
# Author: Tuan Nguyen
# Date created: 20200110
#!242.py
# ----------------------------
"""
You are given an array of length 24, where each element represents the number of new subscribers during the corresponding hour. 

Implement a data structure that efficiently supports the following:
* update(hour: int, value: int): Increment the element at index hour by value.
* query(start: int, end: int): Retrieve the number of subscribers that have signed up between start and end (inclusive).

You can assume that all values get cleared at the end of the day, and that you will not be asked for start and end values that wrap around midnight.
"""


class Subscriber:
    """a data structure"""

    def __init__(self):
        """constructor: create an array of length 24"""
        self._data = [
            0 for i in range(24)
        ]  # each element represents the number of new subscribers during the corresponding hour

    def update(self, hour, value):
        """increment the element at index hour by value"""
        self._data[hour] += value

    def query(self, start, end):
        """retrieve the number of subscribers that have signed up between start and end (inclusive)"""
        retrieve = 0
        for i in range(start, end + 1):
            retrieve += self._data[i]
        return retrieve


# ----- end of Subscriber class -----


def test_Subscriber():
    s = Subscriber()
    s.update(3, 3)
    s.update(7, 7)
    s.update(10, 10)
    assert s.query(3, 7) == 10
    assert s.query(0, 23) == 20


if __name__ == "__main__":
    test_Subscriber()
