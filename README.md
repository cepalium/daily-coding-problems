# Daily Coding Problems

Register to receive Daily Coding Problem everyday [here](https://www.dailycodingproblem.com/). <br/>

Day | Origin | Difficulty | Status
--- | ------ | ---------- | ------ 
[1](#1) | Google | Easy | [1.py](https://github.com/TuanANg/daily-coding-problems/blob/master/solutions/1.py)
[2](#2) | Uber | Hard | [2.py](https://github.com/TuanANg/daily-coding-problems/blob/master/solutions/2.py)
[3](#3) | Google | Medium | UNSOLVED []()
[4](#4) | Stripe | Hard | [4.py](https://github.com/TuanANg/daily-coding-problems/blob/master/solutions/4.py)
[5](#5) | Jane Street | Medium | [5.py](https://github.com/TuanANg/daily-coding-problems/blob/master/solutions/5.py)
[6](#6) | Google | Hard | UNSOLVED []()
[7](#7) | Facebook | Medium | [7.py](https://github.com/TuanANg/daily-coding-problems/blob/master/solutions/7.py)
[8](#8) | Google | Easy | UNSOLVED []()
[9](#9) | Airbnb | Hard | [9.py](https://github.com/TuanANg/daily-coding-problems/blob/master/solutions/9.py)
[10](#10) | Apple | Medium | UNSOLVED []()
[11](#11) | Twitter | Meidum | [11.py](https://github.com/TuanANg/daily-coding-problems/blob/master/solutions/11.py)
[12](#12) | Amazon | Hard | UNSOLVED []()
[13](#13) | Amazon | Hard | [13.py](https://github.com/TuanANg/daily-coding-problems/blob/master/solutions/13.py)
[14](#14) | Google | Medium | [14.py](https://github.com/TuanANg/daily-coding-problems/blob/master/solutions/14.py)
[15](#15) | Facebook | Medium | UNSOLVED []()

## Problem descriptions

### #1

Given a list of numbers and a number k, 
return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, 
return true since 10 + 7 is 17.

---

### #2

Given an array of integers , return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, 
<li> if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24] </li>
<li>If our input was [3, 2, 1], the expected output would be [2, 3, 6]

---

### #3

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

### #4

Given an array of integers (The array can contain duplicates and negative numbers as well.)<br/>
Find the first missing positive integer in linear time and constant space, i.e find the lowest positive integer that does not exist in the array.

For example, the input [3, 4, -1, 1] should give 2. <br/>
The input [1, 2, 0] should give 3.

---

### #5

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

### #6

An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.

---

##3 #7

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.

---

### #8

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

 ### #9

Given a list of integers, 
write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. 
[5, 1, 1, 5] should return 10, since we pick 5 and 5.

---

### #10

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

---

### #11

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

---

### #12

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. 
Given N, write a function that returns the number of unique ways you can climb the staircase. 
The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:
* 1, 1, 1, 1
* 2, 1, 1
* 1, 2, 1
* 1, 1, 2
* 2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? 
For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

---

### #13

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

---

### #14

The area of a circle is defined as πr<sup>2</sup>. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x<sup>2</sup> + y<sup>2</sup> = r<sup>2</sup>.

---

### #15

Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.

---
