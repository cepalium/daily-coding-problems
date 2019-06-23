# ------------------------------------
# Author: Tuan Nguyen
# Date: 20190623
#!solutions/41.py
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

def computeItinerary(flights, start):
# input: list 'flights' of flights(start, destination) & starting airport 'start'
# output: return the lexicographically smallest itineriries
# e.g flights = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')], start = 'A' 
# ~> return ['A', 'B', 'C', 'A', 'C'] // ['A', 'C', 'A', 'B', 'C'] is also valid but a bigger one
    route = []  # init itinerary
    source = dest = start   # init source
    while flights:  # loop until list 'flights' has no flight
        route.append(source)
        destList = [flight[1] for flight in flights if flight[0] == source]
        if not destList:    # if no flight availble from source, then break loop
            break
        dest = min(destList)    # else, then choose the lexicographically smallest destnation
        flights.remove((source, dest))  # remove this flight from list 'flights'
        source = dest
    if not flights: # make up the iterary successully w/ all flights
        return route
    return 'No itinerary available' # else


def computeItinerary_test(flights, start):
    print('flights: ', flights, ', start: ', start, end =' ')
    print(' -> Itinerary: ', computeItinerary(flights, start))


if __name__ == "__main__":
    computeItinerary_test([('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')], 'YUL') # return ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']
    computeItinerary_test([('SFO', 'COM'), ('COM', 'YYZ')], 'COM')  # return null
    computeItinerary_test([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')], 'A')    # return ['A', 'B', 'C', 'A', 'C']
