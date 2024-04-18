# ----------------------------
# Author: Tuan Nguyen
# Date created: 20200219
#!282.py
# ----------------------------
"""
Given an array of integers, determine whether it contains a Pythagorean triplet. 
Recall that a Pythogorean triplet (a, b, c) is defined by the equation a2+ b2= c2.
"""


def pythagorean_triplet(arr):
    """return True if array contains a Pythagorean triplet; otherwise False"""
    n = len(arr)
    if n < 2:  # trivial case
        return False
    a = [i**2 for i in arr]  # square elements in arr
    a.sort()  # sort a
    for i in range(
        n - 1, 1, -1
    ):  # index of c2; last i is 2 s.t a2=a[0], b2=a[1], c2=a[2]
        l = 0  # index of a2
        r = i - 1  # index of b2
        while l < r:
            if a[i] > a[l] + a[r]:  # c2 > a2 + b2
                l += 1  # l moves left 1 position to have bigger a2
            elif a[i] < a[l] + a[r]:  # c2 < a2 + b2
                r -= 1  # r moves right 1 position to have smaller b2
            else:  # find triplet
                return True
    return False  # reach this means no pythagorean triplet found


def test1():
    assert pythagorean_triplet([1, 2, 3, 4, 5]) == True


def test2():
    assert pythagorean_triplet([1, 2, 3, 4, 6]) == False


def test3():
    assert pythagorean_triplet([6, 8, 10]) == True


def test4():
    assert pythagorean_triplet([1]) == False


def test5():
    assert pythagorean_triplet([-1, -2, -3, -4, -5]) == True


if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()
