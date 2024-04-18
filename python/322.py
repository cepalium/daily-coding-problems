# --------------------------
# Author: Tuan Nguyen
# Date created: 20200330
#!322.py
# --------------------------
"""
Starting from 0 on a number line, you would like to make a series of jumps that lead to the integer N.

On the ith jump, you may move exactly i places to the left or right.

Find a path with the fewest number of jumps required to get from 0 to N.
"""


def fewest_jump_path(N):
    """return a list of integers
    s.t indicating a path with the fewest number of jumps from 0 to N"""
    # trivial case
    if N == 0:
        return [0]
    # else:
    sign = N // abs(N)  # -1 if N is negative; 1 otherwise
    N = abs(N)  # consider path only from 0 to positive N
    cur_pos = 0  # current position
    jump = 1  # 1st jump takes 1 step
    path = [0]  # output path from 0 to N, initialized with 0
    while cur_pos != N:
        """if next jump passes N, then jump backward; otherwise, jump forward"""
        if cur_pos + jump <= N:
            cur_pos += jump
        else:
            cur_pos -= jump
        path.append(cur_pos)  # add current position to the shortest path
        jump += 1  # next jump is 1 step further
    if (
        sign == -1
    ):  # switch signs of all positions to have the correct path to negative N
        return [-pos for pos in path]
    return path


# ----- UNIT TESTS -----
def test1():
    assert fewest_jump_path(N=0) == [0]


def test2():
    assert fewest_jump_path(N=1) == [0, 1]


def test3():
    assert fewest_jump_path(N=3) == [0, 1, 3]


def test4():
    assert fewest_jump_path(N=4) == [0, 1, 3, 0, 4]


def test5():
    assert fewest_jump_path(N=-2) == [0, -1, 1, -2]


def test6():
    assert fewest_jump_path(N=-5) == [0, -1, -3, 0, -4, 1, -5]


if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
