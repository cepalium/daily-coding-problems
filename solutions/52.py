
# -----------------------------------
# Author: Tuan Nguyen
# Date: 2090704
#!solutions/52.py
# -----------------------------------
"""
Implement an LRU (Least Recently Used) cache. 
It should be able to be initialized with a cache size n, and contain the following methods:

set(key, value): sets key to value. 
If there are already n items in the cache and we are adding a new item, 
then it should also remove the least recently used item.
get(key): gets the value at key. If no such key exists, return null.
"""

import collections

'''
Class: Least-Recently-Used Cache
'''
class LRUCache():
    def __init__(self, size):
        self.size = size
        self.deq = collections.deque()  # init double-ended queue: store key ~> LRU element in last
        self.dict = {}  # init dict(): store (key,value)
    
    '''
    Functionality: sets key to value
    * If there are already n items in the cache and we are adding a new item, then it should also remove the least recently used item.
    '''
    def set(self, key, value):
        if len(self.deq) == self.size:  # if cache is full
            lru_key = self.deq.pop()    # get rid of the LRU element by popping the last element in deq
            del(self.dict[lru_key])     # delete (key,value) in dict
        self.deq.appendleft(key)    # add key to front of deq, i.e most-recently used
        self.dict[key] = value  # save value of key
    
    '''
    Functionality: gets the value at key
    * If no such key exists, return null
    '''
    def get(self, key):
        if key in self.dict.keys():
            return self.dict[key]
        return None


def main():
    cache = LRUCache(size=3)    # init LRU cache
    cache.set(1, 10)    # add (1,10) ~> dict {1:10}
    cache.set(2, 20)    # add (2,20) ~> dict {1:10, 2:20}
    cache.set(3, 30)    # add (3,30) ~> dict {1:10, 2:20, 3:30}
    print(cache.dict)   # print dict {1:10, 2:20, 3:30}
    cache.set(4, 40)    # remove LRU element, i.e (1,10) ~> dict {2:20, 3:30, 4:40}
    cache.set(5, 50)    # remove LRU element, i.e (2,20) ~> dict {3:30, 4:40, 5:50}
    print(cache.dict)   # print dict {3:30, 4:40, 5:50}
    print(cache.get(1)) # return None b/c no key '1' in cache
    print(cache.get(5)) # return 50


if __name__ == "__main__":
    main()

        