# ------------------------------------
# Author: Tuan Nguyen
# Date created: 20200726
#!41.py
# ------------------------------------
"""
Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, 
and a starting airport, compute the person's itinerary. 
If no such itinerary exists, return null. 
If there are multiple possible itineraries, return the lexicographically smallest one. 
All flights must be used in the itinerary.

For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] 
and starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] 
and starting airport 'COM', you should return null.

Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting airport 'A', 
you should return the list ['A', 'B', 'C', 'A', 'C'] 
even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary. 
However, the first one is lexicographically smaller.
"""
def compute_itinerary(flights, start):
    itinerary = []
    source = start   # init source
    while flights:  # loop until list 'flights' has no flight
        itinerary.append(source)
        destinations = [dest for (src, dest) in flights if src == source]
        if not destinations:    # if no flight availble from source, then break loop
            break
        min_dest = min(destinations)  # lexicographically smallest destnation
        flights.remove((source, min_dest))
        source = min_dest
    itinerary.append(source)  # add the destination of the last flight
    if not flights:  # make up the iterary successully w/ all flights
        return itinerary
    return None


def test1():
    assert compute_itinerary([('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')], 'YUL') == ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']

def test2():
    assert compute_itinerary([('SFO', 'COM'), ('COM', 'YYZ')], 'COM') == None

def test3():
    assert compute_itinerary([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')], 'A') == ['A', 'B', 'C', 'A', 'C']

if __name__ == "__main__":
    test1()
    test2()
    test3()