# --------------------------
# Author: Tuan Nguyen
# Date: 20190518
# Task: Given a pair (a,b) constructed by cons(a,b), 
# implement car(cons(a,b) to return the first element of the pair i.e a 
# and cdr(cons(a,b)) to return the last element of the pair i.e b.
# --------------------------

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


def unitTest(a, b):
    print((a,b), car(cons(a,b)), cdr(cons(a,b)))


if __name__ == "__main__":
    unitTest(3,4)
    unitTest(5,6)
    unitTest(-1,1)