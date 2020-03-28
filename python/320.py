# --------------------------
# Author: Tuan Nguyen
# Date created: 20200328
#!320.py
# --------------------------
"""
Given a string, find the length of the smallest window that contains every distinct character. 
Characters may appear more than once in the window.

For example, given "jiujitsu", you should return 5, corresponding to the final five letters.
"""
def smallest_distinct_window(string):
    """ return the length of the smallest window that contains every distinct character """
    #trivial cases
    if len(string) == 0:
        return 0
    if len(string) == 1:
        return 1
    # normal cases
    w = list()  # window as queue
    w.append(string[0])  # window started 
    for c in string[1:]:
        if c == w[0]:
            w.pop(0)
        w.append(c)
    return len(w)

# ----- UNIT TEST -----
def test1():
    assert smallest_distinct_window("") == 0

def test2():
    assert smallest_distinct_window("a") == 1

def test3():
    assert smallest_distinct_window("aa") == 1

def test4():
    assert smallest_distinct_window("jiujitsu") == 5

def test5():
    assert smallest_distinct_window("jiujjits") == 6

if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()