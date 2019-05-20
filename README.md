# Daily Coding Problems

Register to receive Daily Coding Problem everyday [here](https://www.dailycodingproblem.com/). <br/>
My solutions are written in Python3.

---

## #1  @20190514

Status: SOLVED [1.py](https://github.com/TuanANg/daily-coding-problems/blob/master/solutions/1.py)

Given a list of numbers and a number k <br/>
Return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, 
return true since 10 + 7 is 17.

---

## #2 @20190515

Status: SOLVED [2.py](https://github.com/TuanANg/daily-coding-problems/blob/master/solutions/2.py)

Given an array of integers <br/>
Return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, 
<li> if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24] </li>
<li>If our input was [3, 2, 1], the expected output would be [2, 3, 6]

---

## #3 @20190516

Status: UNSOLVED []()

Given the root to a binary tree, 
implement serialize(root), which serializes the tree into a string, 
and deserialize(s), which deserializes the string back into the tree.

Example: given a Node class <br/>
```
class Node:
   def __init__(self, val, left=None, right=None):
       self.val = val
        self.left = left
        self.right = right
```
The following test should pass: <br/>
>node = Node('root', Node('left', Node('left.left')), Node('right'))<br/>
>assert deserialize(serialize(node)).left.left.val == 'left.left'

---

## #4 @20190517

Status: SOLVED [4.py](https://github.com/TuanANg/daily-coding-problems/blob/master/solutions/4.py)

Given an array of integers (The array can contain duplicates and negative numbers as well.)<br/>
Find the first missing positive integer in linear time and constant space, i.e find the lowest positive integer that does not exist in the array.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

---

## #5 @20190518

Status: SOLVED [5.py](https://github.com/TuanANg/daily-coding-problems/blob/master/solutions/5.py)

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:
```
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
```
Implement car and cdr.

---

## #6 @20190519

Status: UNSOLVED []()

An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.

---

## #7 @20190520

Status: SOLVED [7.py](https://github.com/TuanANg/daily-coding-problems/blob/master/solutions/7.py)

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.

---