# -----------------------------
# Author: Tuan Nguyen
# Date: 20190802
#!solutions/81.py
# -----------------------------
"""
Given a mapping of digits to letters (as in a phone number), and a digit string, 
return all possible letters the number could represent. You can assume each valid number in the mapping is a single digit.

For example if {“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …} 
then “23” should return [“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"].
"""

# global dictionary of mapping digits to letters
digitsToLetters = {
    "0": [""],
    "1": [""],
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
}


def possibleWords(digitStr):
    # input: 1 string of digit 'digitStr'
    # output: list of all possible letters the number could represent
    # trivial case
    if not digitStr:
        return []
    # init: output list w/ letters of last digit, then discard the last digit from input
    words = [c for c in digitsToLetters[digitStr[-1]]]
    digitStr = digitStr[:-1]
    # iteration
    while digitStr:  # until all digits
        lastDigit = digitStr[-1]
        tmp = []  # temporary list to store new concated words
        for c in digitsToLetters[
            lastDigit
        ]:  # add letters from current last digits to all words in current list 'words'
            for word in words:
                word = c + word
                tmp.append(word)
        words = tmp.copy()  # copy new words to list 'words'
        digitStr = digitStr[:-1]  # discard the current last digit
    return words


def possibleWords_test(digitStr):
    print(digitStr, "~>", possibleWords(digitStr))


if __name__ == "__main__":
    possibleWords_test(
        "23"
    )  # return [“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"]
    possibleWords_test("2")  # return ['a', 'b', 'c']
    possibleWords_test("")  # return []
    possibleWords_test(
        "69"
    )  # return ['mw', 'mx', 'my', 'mz', 'nw', 'nx', 'ny', 'nz', 'ow', 'ox', 'oy', 'oz']
