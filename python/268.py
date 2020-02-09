# ----------------------------
# Author: Tuan Nguyen
# Date created: 20200209
#!268.py
# ----------------------------
"""
Given a 32-bit positive integer N, 
determine whether it is a power of four in faster than O(log N) time.
"""
import math

def is_power_of_four(N):
    """ return True if N is a power of 4, else False """
    if N == 0:
        return False
    log_4_N = math.log(N, 4)
    if log_4_N % 1 == 0:    # if log(N) is integer
        return True
    else:
        return False

def test1():
    assert is_power_of_four(0) == False

def test2():
    assert is_power_of_four(1) == True

def test3():
    assert is_power_of_four(2) == False

def test4():
    assert is_power_of_four(4) == True

def test5():
    assert is_power_of_four(5) == False

if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()