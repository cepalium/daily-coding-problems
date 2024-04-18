# --------------------------
# Author: Tuan Nguyen
# Date created: 20200409
#!332.py
# --------------------------
"""
Given integers M and N, write a program that counts how many positive integer pairs (a, b) satisfy the following conditions:

* a + b = M
* a XOR b = N
"""


def num_positive_pairs(M, N):
    """return the number of positive integer pairs (a,b) s.t a + b = M & a XOR b = N"""
    if M < 0 and N < 0:  # trivial case
        return 0
    num_pairs = 0
    for a in range(1, M):
        b = M - a
        if b < 0:
            break
        if a ^ b == N:
            num_pairs += 1
    return num_pairs


def test1():
    assert num_positive_pairs(M=2, N=0) == 1


def test2():
    assert num_positive_pairs(M=3, N=3) == 2


if __name__ == "__main__":
    test1()
    test2()
