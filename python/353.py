# --------------------------
# Author: Tuan Nguyen
# Date created: 20200426
#!349.py
# --------------------------
"""
You are given a histogram consisting of rectangles of different heights. 
These heights are represented in an input list, such that [1, 3, 2, 5] corresponds to the following diagram:

      x
      x  
  x   x
  x x x
x x x x

Determine the area of the largest rectangle that can be formed only from the bars of the histogram. 
For the diagram above, for example, this would be six, representing the 2 x 3 area at the bottom right.
"""
def largest_area(histogram):
    if len(histogram) == 0:  # trivial cases
        return 0
    if len(histogram) == 1:
        return histogram[0]
    max_height, min_height = max(histogram), min(histogram)
    max_area = 0
    for h in range(min_height, max_height+1):
        w = max_width_with_height(histogram, h)
        a = h * w
        if max_area < a:
            max_area = a
    return max_area

def max_width_with_height(histogram, height):
    max_width, current_width = 0, 0
    for h in histogram:
        if h >= height:  # update current width
            current_width += 1
        else:
            current_width = 0
        if current_width > max_width:  # update max width
                max_width = current_width
    return max_width

def test1():
    assert largest_area([]) == 0

def test2():
    assert largest_area([3]) == 3

def test3():
    assert largest_area([1, 3, 2, 5]) == 6

def test4():
    assert largest_area([100, 3, 2, 5]) == 100

def test5():
    assert largest_area([2, 4, 6, 8]) == 12

if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()