# -------------------------------
# Author: Tuan Nguyen
# Date: 20190611
#!solutions/29.py
# -------------------------------
"""
Run-length encoding is a fast and simple method of encoding strings. 
The basic idea is to represent repeated successive characters as a single count and character. 
For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. 
You can assume the string to be encoded have no digits and consists solely of alphabetic characters. 
You can assume the string to be decoded is valid.
"""


def runLengthEncoding(string):
# input: string string
# output: run-length encoding string encodingString
    encodingString = ""     # init output string
    curLetter = string[0]   # init current letter
    pivot = 0               # init pivot
    for i in range(1, len(string)):
        if string[i] != curLetter:
            encodingString += str(i - pivot) + curLetter    # count & character
            pivot = i
            curLetter = string[i]
        if i == len(string) - 1:    # last letter in string
            encodingString += str(len(string) - pivot) + curLetter
    return encodingString


def runLengthEncoding_test(string):
    print(string, runLengthEncoding(string))


if __name__ == "__main__":
    runLengthEncoding_test("AAAABBBCCDAA")  # return "4A3B2C1D2A"
    runLengthEncoding_test("AAAABBBCCDA")  # return "4A3B2C1D1A"
    runLengthEncoding_test("AAAAAAA")  # return "7A"
    runLengthEncoding_test("ABCD")  # return "1A1B1C1D"