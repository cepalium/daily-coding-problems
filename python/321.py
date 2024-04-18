# --------------------------
# Author: Tuan Nguyen
# Date created: 20200329
#!321.py
# --------------------------
"""
Given a positive integer N, find the smallest number of steps it will take to reach 1.

There are two kinds of permitted steps:
You may decrement N to N - 1.
If a * b = N, you may decrement N to the larger of a and b.

For example, given 100, you can reach 1 in five steps with the following route: 100 -> 10 -> 9 -> 3 -> 2 -> 1.
"""


def smallest_steps_to_1(N):
    """return the smallest number of steps for N to reach 1"""
    # handle error and trivial case
    if N < 1:
        raise ValueError("N must be greater or equal to 1")
    if N == 1:
        return 0
    """
    Rank of fastest ways to reduce N to 1:
    1. Take root square of N
    2. Divide N by its greatest divisor
    3. Decrease N by 1
    """
    num_step = 0
    while N > 1:
        if N == 2:  # 2 -> 1: 1 step from 2 to 1
            num_step += 1
            break
        if N == 3:  # 3 -> 2 -> 1: 2 steps from 3 to 1
            num_step += 2
            break
        sqrt_N = N**0.5
        if sqrt_N == int(sqrt_N):  # N is a perfect square
            N = int(sqrt_N)
        else:
            divisors = [i for i in range(int(sqrt_N), 1, -1) if N % i == 0]
            if divisors:  # N has at least 1 divisor [sqrt N, 3]
                N = N // divisors[0]
            else:  # better substract N by 1 for next step
                N -= 1
        num_step += 1
    return num_step


# ----- UNIT TESTS -----
def test1():
    assert smallest_steps_to_1(N=1) == 0


def test2():
    assert smallest_steps_to_1(N=2) == 1


def test3():
    assert smallest_steps_to_1(N=3) == 2


def test4():
    assert smallest_steps_to_1(N=99) == 5


def test5():
    assert smallest_steps_to_1(N=100) == 5


if __name__ == "__main__":
    test1()
