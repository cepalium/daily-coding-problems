# ------------------------
# Author: Tuan Nguyen
# Date created: 20191201
#!202.py
# ------------------------
"""
Write a program that checks whether an integer is a palindrome. 
For example, 121 is a palindrome, as well as 888. 678 is not a palindrome. 
Do not convert the integer into a string.
"""

def is_number_palindrome(n):
    """ return True if int n is a palindrome """
    digits = list()     # list of all digits in n (reversed order)
    while n > 0:
        last_digit = n % 10
        digits.append(last_digit)
        n = n // 10
    if is_list_palindrome(digits):
        return True
    else:
        return False

def is_list_palindrome(lst):
    """ return True if list is palindrome """
    n = len(lst)
    for i in range(n//2):           # go until middle of list
        if lst[i] != lst[-1 - i]:   # a pair of elements doesn't match
            return False
    return True


def test_is_number_palindrome():
    assert is_number_palindrome(121) == True
    assert is_number_palindrome(888) == True
    assert is_number_palindrome(678) == False

if __name__ == "__main__":
    test_is_number_palindrome()