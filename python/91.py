# ------------------------------
# Author: Tuan Nguyen
# Date: 20190812
#!solutions/91.py
# -------------------------------
"""
What does the below code snippet print out? How can we fix the anonymous functions to behave as we'd expect?

functions = []
for i in range(10):
    functions.append(lambda : i)

for f in functions:
    print(f())
"""

functions = []
for i in range(10):
    functions.append(lambda: i)

i = 0
for f in functions:
    print(f())
    i += 1
