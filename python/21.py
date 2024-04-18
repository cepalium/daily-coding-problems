# ---------------------------
# Author: Tuan Nguyen
# Date: 20190603
#!solutions/21.py
# ---------------------------
"""
Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), 
find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""


def minRoomRequired(lectures):
    # input: list lectures of tuples(start, end)
    # output: minimum number of rooms required
    curRoom = 0
    minRoom = 0
    eventList = []
    for lecture in lectures:
        eventList.append(
            [lecture[0], "i"]
        )  # add start as 'i' event, i.e 'i' for 'in
        eventList.append(
            [lecture[1], "o"]
        )  # add end as 'o' event, i.e 'o' for out
    eventList.sort(key=lambda x: x[0])  # sort event list by time
    for e in eventList:
        eventType = e[1]  # event type: 'i' or 'o'
        if eventType == "i":  # if lecture starts, 1 more room is required
            curRoom += 1
        if eventType == "o":  # if lecture ends, 1 room is free
            curRoom -= 1
        if curRoom > minRoom:  # minRoom = max currently-in-use number of rooms
            minRoom = curRoom
    return minRoom


def minRoomRequired_test(lectures):
    print(lectures, minRoomRequired(lectures))


if __name__ == "__main__":
    minRoomRequired_test([(30, 75), (0, 50), (60, 150)])  # return 2
    minRoomRequired_test([(30, 75), (0, 100), (60, 150)])  # return 3
