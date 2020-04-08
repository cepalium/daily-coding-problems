# --------------------------
# Author: Tuan Nguyen
# Date created: 20200408
#!331.py
# --------------------------
"""
You are given a string consisting of the letters x and y, such as xyxxxyxyy. 
In addition, you have an operation called flip, which changes a single x to y or vice versa.

Determine how many times you would need to apply this operation to ensure that all x's come before all y's. 
In the preceding example, it suffices to flip the second and sixth characters, so you should return 2.
"""
def flip_x_before_y(str):
    """ return the number of flip to have all x before all y in string """
    if len(str) < 2:  # trivial cases: length 0 or 1
        return 0
    start_flip = False
    num_flips = 0
    for c in str[::-1]:
        if c != 'x' and c != 'y':
            raise ValueError("String can contain 'x' or 'y' only.")
        if c == 'x' and start_flip == False:
            start_flip = True
            continue
        if c == 'y' and start_flip == True:
            num_flips += 1
            continue
    return num_flips

# ----- UNIT TESTS -----
def test1():
    assert flip_x_before_y("") == 0

def test2():
    assert flip_x_before_y("y") == 0

def test3():
    assert flip_x_before_y("xxx") == 0

def test4():
    assert flip_x_before_y("xyx") == 1

def test5():
    assert flip_x_before_y("xyxxxyxyy") == 2

if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()