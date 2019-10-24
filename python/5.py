# --------------------------
# Author: Tuan Nguyen
# Date: 20190518
# --------------------------
"""
Problem: 

cons(a, b) constructs a pair, 
and car(pair) and cdr(pair) returns the first and last element of that pair. 

For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
"""


def cons(a, b):
# input: 2 ints a&b
# output: 
    return lambda f: f(a,b)


def car(f):
# input:
# output: first element of a pair
    return f(lambda a,b: a)


def cdr(f):
# input:
# output: last element of a pair
    return f(lambda a,b: b) 


def car_cdr_test(a, b):
    print((a,b), car(cons(a,b)), cdr(cons(a,b)))


if __name__ == "__main__":
    car_cdr_test(3,4)   # return 3, 4
    car_cdr_test(5,6)   # return 5, 6
    car_cdr_test(-1,1)  # return -1, 1