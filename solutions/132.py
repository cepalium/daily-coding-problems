# ------------------------------
# Author: Tuan Nguyen
# Date created: 20190924
#!solutions/132.py
# ------------------------------
"""
Design and implement a HitCounter class that keeps track of requests (or hits). 
It should support the following operations:
* record(timestamp): records a hit that happened at timestamp
* total(): returns the total number of hits recorded
* range(lower, upper): returns the number of hits that occurred between timestamps lower and upper (inclusive)

Follow-up: What if our system has limited memory?
"""

class HitCounter:
    def __init__(self):
        self.data = []
        self.size = 0
    
    """ records a hit that happened at timestamp """
    def record(self, timestamp):
        j = 0
        while j < self.size:
            if timestamp > self.data[j]:
                j += 1
        self.data.insert(j, timestamp)
        self.size += 1


    
    """ returns the total no. hits recorded """
    def total(self):
        return self.size
    

    """ returns no. hits the occured between timestamps lower and upper (inclusive) """
    def range(self, lower, upper):
        if lower > upper:
            raise Exception("Invalid input")
        lowerIndex = self.binarySearch(self.data, lower, 0, self.size-1)
        upperIndex = self.binarySearch(self.data, upper, 0, self.size-1)
        if self.data[lowerIndex] < lower and lowerIndex < self.size-1:  # not include the smaller element of lower value
            lowerIndex += 1
        if self.data[upperIndex] == upper:  # include the upper value
            upperIndex += 1
        return upperIndex - lowerIndex

    
    """ returns index of desired value in array """
    def binarySearch(self, data, val, low, high):
        if low >= high:
            return low
        mid = (low + high) // 2
        if data[mid] == val:
            return mid
        elif data[mid] > val:
            return self.binarySearch(data, val, low, mid-1)
        else:
            return self.binarySearch(data, val, mid+1, high)


def main():
    hits = HitCounter()
    for i in range(1, 11):
        hits.record(i)          # hit counter [1, 2, ..., 10]
    print(hits.total())         # print 10
    print(hits.range(4,10))     # print 7
    print(hits.range(4.5,8.5))  # print 4
    print(hits.range(-5,2))     # print 2
    print(hits.range(-2, 2.5))  # print 2
    print(hits.range(-5, -2))   # print 0
    print(hits.range(15, 20))   # print 0
    

if __name__ == "__main__":
    main()
