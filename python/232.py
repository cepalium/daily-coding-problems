# -------------------------
# Author: Tuan Nguyen
# Date created: 20200102
#!232.py
# -------------------------
"""
Implement a PrefixMapSum class with the following methods:

* insert(key: str, value: int): Set a given key's value in the map. If the key already exists, overwrite the value.
* sum(prefix: str): Return the sum of all values of keys that begin with a given prefix.

For example, you should be able to run the following code:

mapsum.insert("columnar", 3)
assert mapsum.sum("col") == 3

mapsum.insert("column", 2)
assert mapsum.sum("col") == 5
"""


class PrefixMapSum:
    """ """

    def __init__(self):
        """intialize empty map sum"""
        self.map_sum = dict()

    def insert(self, key, value):
        """set value for given key; overwrite if key exists"""
        self.map_sum[key] = value

    def sum(self, prefix):
        """return the sum of all values of keys that begin with a given prefix"""
        total = 0
        n = len(prefix)
        for k, v in self.map_sum.items():
            if k[:n] == prefix:
                total += v
        return total


# ----- end of PrefixMapSum class -----


def test_PrefixMapSum():
    mapsum = PrefixMapSum()

    mapsum.insert("columnar", 3)
    assert mapsum.sum("col") == 3

    mapsum.insert("column", 2)
    assert mapsum.sum("col") == 5


if __name__ == "__main__":
    test_PrefixMapSum()
