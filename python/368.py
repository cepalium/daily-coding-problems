# -------------------------------
# Author: Tuan Nguyen
# Date created: 20200518
#!368.py
# -------------------------------
"""
Implement a key value store, where keys and values are integers, with the following methods:

* update(key, vl): updates the value at key to val, or sets it if doesn't exist
* get(key): returns the value with key, or None if no such value exists
* max_key(val): returns the largest key with value val, or None if no key with that value exists

For example, if we ran the following calls:
```
kv.update(1, 1)
kv.update(2, 1)
```

And then called kv.max_key(1), it should return 2, since it's the largest key with value 1.
"""


class KeyValueStore:
    def __init__(self):
        self.key_value_dict = dict()
        self.max_value_dict = dict()

    def update(self, key, value):
        self.key_value_dict[key] = value
        self._update_max_key(key, value)

    def _update_max_key(self, key, value):
        current_key = self.max_value_dict.get(value, None)
        if not current_key:
            self.max_value_dict[value] = key
        elif current_key and current_key < key:
            self.max_value_dict[value] = key

    def get(self, key):
        return self.key_value_dict.get(key, None)

    def max_key(self, val):
        return self.max_value_dict.get(val, None)


def test1():
    kv = KeyValueStore()
    kv.update(1, 1)
    kv.update(2, 1)
    assert kv.max_key(1) == 2
    assert kv.get(1) == 1
    assert kv.get(0) == None


if __name__ == "__main__":
    test1()
