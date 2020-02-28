# ----------------------------
# Author: Tuan Nguyen
# Date created: 20200228
#!291.py
# ----------------------------
"""
An imminent hurricane threatens the coastal town of Codeville. 
If at most two people can fit in a rescue boat, and the maximum weight limit for a given boat is k, determine how many boats will be needed to save everyone.

For example, given a population with weights [100, 200, 150, 80] and a boat limit of 200, the smallest number of boats required will be three.
"""
def min_survival_boats(pop, weight_lim, people_lim=2):
    """ return the minimum number of boats to save all population s.t max people_lim persons/boat & sum human weight < weight_lim """
    n = len(pop)
    if n == 0:    # trivial case
        return 0
    boat = {i: [] for i in range(n)}    # boat[i] stores max 2 weights
    # assign each passenger to suitable boat
    for mass in pop:
        for i in boat.keys():    # find suitable boat for this person
            m = len(boat[i])    # number of people on current boat
            boat_weight = sum(boat[i])    # sum weights on current boat
            if m < people_lim and boat_weight + mass <= weight_lim:
                boat[i].append(mass)
                break
    # count number of occupied boats
    min_boats = 0
    for i in boat.keys():
        if boat[i]:
            min_boats += 1
        else:
            break
    return min_boats

def test1():
    assert min_survival_boats(pop=[100, 200, 150, 80], weight_lim=200, people_lim=2) == 3

def test2():
    assert min_survival_boats(pop=[], weight_lim=100) == 0

def test3():
    assert min_survival_boats(pop=[100, 200, 150, 80], weight_lim=300, people_lim=2) == 2

def test4():
    assert min_survival_boats(pop=[100, 200, 150, 80], weight_lim=600, people_lim=10) == 1

def test5():
    assert min_survival_boats(pop=[100, 20, 80], weight_lim=100, people_lim=2) == 2

if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()