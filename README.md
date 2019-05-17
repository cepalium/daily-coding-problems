# Daily Coding Problems

Register to receive Daily Coding Problem every [here](https://www.dailycodingproblem.com/). <br/>
My solutions are written in Python3.

---

## #1  @20190514
Given a list of numbers and a number k <br/>
Return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, 
return true since 10 + 7 is 17.

---

## #2 @20190515
Given an array of integers <br/>
Return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, 
<li> if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24] </li>
<li>If our input was [3, 2, 1], the expected output would be [2, 3, 6]

---

## #3 @20190516
Given the root to a binary tree, 
implement serialize(root), which serializes the tree into a string, 
and deserialize(s), which deserializes the string back into the tree.

Example: given a Node class <br/>
```
class Node: <br/>
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
Given an array of integers (The array can contain duplicates and negative numbers as well.)<br/>
Find the first missing positive integer in linear time and constant space, i.e find the lowest positive integer that does not exist in the array.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

---

