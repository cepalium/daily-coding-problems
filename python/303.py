# ----------------------------
# Author: Tuan Nguyen
# Date created: 20200321
#!303.py
# ----------------------------
"""
Given a clock time in hh:mm format, 
determine, to the nearest degree, the angle between the hour and the minute hands.

Bonus: When, during the course of a day, will the angle be zero?
"""
import time

def calculate_angle_hour_minute(time_string):
    """ return the angle between hour and minute hands in degree from hh:mm """
    timestamp = time.strptime(time_string, '%H:%M')
    h = timestamp.tm_hour
    m = timestamp.tm_min
    hour_angle = (h % 12 + m / 60) * 30
    minute_angle = (m / 60) * 360
    return abs(hour_angle - minute_angle)

def test1():
    assert calculate_angle_hour_minute('01:30') == 135

def test2():
    assert calculate_angle_hour_minute('00:00') == 0

def test3():
    assert calculate_angle_hour_minute('12:00') == 0

def test4():
    assert calculate_angle_hour_minute('04:30') == 45

def test5():
    assert calculate_angle_hour_minute('23:30') == 165

def test6():
    assert calculate_angle_hour_minute('12:30') == 165

if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()