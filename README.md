# Daily Coding Problems

Register to receive Daily Coding Problem everyday [here](https://www.dailycodingproblem.com/). <br/>
My solutions are written in Python3.

---

## #1

Status: SOLVED [1.py](https://github.com/TuanANg/daily-coding-problems/blob/master/solutions/1.py)

Origin: Google

Level: Easy

Given a list of numbers and a number k, 
return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, 
return true since 10 + 7 is 17.

---

## #2

Status: SOLVED [2.py](https://github.com/TuanANg/daily-coding-problems/blob/master/solutions/2.py)

Origin: Uber

Level: Hard

Given an array of integers , return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, 
<li> if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24] </li>
<li>If our input was [3, 2, 1], the expected output would be [2, 3, 6]

---

## #3

Status: UNSOLVED []()

Origin: Google

Level: Medium

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

## #4

Status: SOLVED [4.py](https://github.com/TuanANg/daily-coding-problems/blob/master/solutions/4.py)

Origin: Stripe

Level: Hard

Given an array of integers (The array can contain duplicates and negative numbers as well.)<br/>
Find the first missing positive integer in linear time and constant space, i.e find the lowest positive integer that does not exist in the array.

For example, the input [3, 4, -1, 1] should give 2. <br/>
The input [1, 2, 0] should give 3.

---

## #5

Status: SOLVED [5.py](https://github.com/TuanANg/daily-coding-problems/blob/master/solutions/5.py)

Origin: Jane Street

Level: Medium

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

## #6

Status: UNSOLVED []()

Origin: Google

Level: Hard

An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.

---

## #7

Status: SOLVED [7.py](https://github.com/TuanANg/daily-coding-problems/blob/master/solutions/7.py)

Origin: Facebook

Level: Medium

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.

---
## #8

Status: UNSOLVED []()

Origin: Google

Level: Easy

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:
```
   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
 ```
 ---

 ## #9

Status: SOLVED [9.py](https://github.com/TuanANg/daily-coding-problems/blob/master/solutions/9.py) 

Origin: Airbnb

Level: Hard

Given a list of integers, 
write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. 
[5, 1, 1, 5] should return 10, since we pick 5 and 5.

---

## #10

Status: UNSOLVED []()

Origin: Apple

Level: Medium

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

---

## #11

Status: SOLVED [11.py](https://github.com/TuanANg/daily-coding-problems/blob/master/solutions/11.py)

Origin: Twitter

Level: Medium

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

---