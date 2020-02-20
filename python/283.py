# -------------------------------
# Author: Tuan Nguyen
# Date created: 20200220
#!283.py
# -------------------------------
"""
A regular number in mathematics is defined as one which evenly divides some power of 60. 
Equivalently, we can say that a regular number is one whose only prime divisors are 2, 3, and 5.

These numbers have had many applications, from helping ancient Babylonians keep time to tuning instruments according to the diatonic scale.

Given an integer N, write a program that returns, in order, the first N regular numbers.
"""
def regular_numbers(N):
    """ return list of first N regular numbers """
    if N == 0:
        return []
    if N == 1:
        return [1]
    p2, p3, p5 = [1], [1], [1]    # list of 2^i, 3^j, 5^k initialized i=j=k=0
    for i in range(1, N):    # calcualte x^i = x^(i-1) * x ~> faster than using power
        p2.append(p2[i-1]*2)
        p3.append(p3[i-1]*3)
        p5.append(p5[i-1]*5)
    p23 = [i*j for i in p2 for j in p3]    # product of p2 & p3
    p25 = [i*k for i in p2 for k in p5]    # product of p2 & p5
    p35 = [j*k for j in p3 for k in p5]    # product of p3 & p5
    p235 = [ij*k for ij in p23 for k in p5]    # product of p2, p3 & p5
    reg_num = sorted(set(p2 + p3 + p5 + p23 + p25 + p35 + p235))
    return reg_num[:N]    # return first N regular numbers

def test1():
    assert regular_numbers(5) == [1, 2, 3, 4, 5]

def test2():
    assert regular_numbers(1) == [1]

def test3():
    assert regular_numbers(10) == [1, 2, 3, 4, 5, 6, 8, 9, 10, 12]

def test4():
    assert regular_numbers(0) == []

def test5():
    assert regular_numbers(3) == [1, 2, 3]

if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()