# -----------------------------------------
# Author: Tuan Nguyen
# Date: 20190615
#!solutions/34.py
# -----------------------------------------
"""
Given a string, find the palindrome that can be made 
by inserting the fewest number of characters as possible anywhere in the word. 
If there is more than one palindrome of minimum length that can be made, 
return the lexicographically earliest one (the first one alphabetically).

For example, given the string "race", you should return "ecarace", 
since we can add three letters to it (which is the smallest amount to make a palindrome). 
There are seven other palindromes that can be made from "race" by adding three letters, 
but "ecarace" comes first alphabetically.

As another example, given the string "google", you should return "elgoogle".
"""


def isPalindrome(string):
    # input: a string string
    # output: True/False if string is a palindrome string
    # palindrome string := reversed string is the same as original string, e.g "level"
    for i in range(
        int(len(string) / 2)
    ):  # check if half left is identical to half right
        if string[i] != string[-i - 1]:
            return False
    return True


def isPalindrome_test(string):
    print(string, ":Palindrome? ", isPalindrome(string))


def makePalindrome(string):
    # input: a string string
    # output: the fewest character-inserting palindrome string
    if isPalindrome(string):  # input string is palindrome at the beginning
        return string
    # if not -> need to add characters to create a palindrome string
    palindromeList = []
    reverse = string[::-1]
    for i in range(len(string)):
        # add in front of input string
        newString = reverse + string[i:]
        if isPalindrome(newString):
            palindromeList.append(newString)
        # add in back of input string
        newString = string + reverse[i:]
        if isPalindrome(newString):
            palindromeList.append(newString)
    # sort palindromeList
    palindromeList.sort()  # sort by alphabetical order
    palindromeList.sort(key=len)  # sort by ascending length
    return palindromeList[
        0
    ]  # return the alphabetically shortest palindrome string


def makePalindrome_test(string):
    print(string, "-> ", makePalindrome(string))


if __name__ == "__main__":
    # isPalindrome
    # isPalindrome_test("abba")   # return True
    # isPalindrome_test("level")  # return True
    # isPalindrome_test("abcdef") # return False

    # makePalindrome
    makePalindrome_test("race")  # return "ecarace"
    makePalindrome_test("google")  # return "elgoogle"
