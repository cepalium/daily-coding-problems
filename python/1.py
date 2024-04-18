# --------------------------
# Author: Tuan Nguyen
# Date created: 20190514
# --------------------------
"""
Problem:

Given a list of numbers and a number k, 
return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, 
return true since 10 + 7 is 17.
"""

from typing import List


def check_sum(arr: List[int], k) -> bool:
    # input: array of numbers & int k
    # output: true/false if any 2 numbers in list add up to k
    for i in range(len(arr) - 1):  # iterate from a[0] to a[len(a)-1]
        for j in range(i + 1, len(arr), 1):  # iterate from a[i+1] to a[-1]
            if k == arr[i] + arr[j]:  # check sum
                return True
    return False


if __name__ == "__main__":
    assert check_sum(arr=[10, 5, 2, 7], k=17) == True
    assert check_sum(arr=[10, 5, 2, 7], k=12) == True
    assert check_sum(arr=[10, 5, 2, 7], k=0) == False
    assert check_sum(arr=[10, 5, 2, 7], k=-5) == False
