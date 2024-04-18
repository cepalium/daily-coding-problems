# --------------------------
# Author: Tuan Nguyen
# Date created: 20200426
#!349.py
# --------------------------
"""
Soundex is an algorithm used to categorize phonetically, such that two names that sound alike but are spelled differently have the same representation.

Soundex maps every name to a string consisting of one letter and three numbers, like M460.

One version of the algorithm is as follows:

1. Remove consecutive consonants with the same sound (for example, change ck -> c).
2. Keep the first letter. The remaining steps only apply to the rest of the string.
3. Remove all vowels, including y, w, and h.
4. Replace all consonants with the following digits:
    * b, f, p, v → 1
    * c, g, j, k, q, s, x, z → 2
    * d, t → 3
    * l → 4
    * m, n → 5
    * r → 6
5. If you don't have three numbers yet, append zeros until you do. Keep the first three numbers.

Using this scheme, Jackson and Jaxen both map to J250.

Implement Soundex.
"""
SOUNDEX_NUMBER_LIMIT = 3


def soundex(name):
    """return the mapping string of the input name based on Soundex algorithm"""
    if len(name) == 0:
        return ""
    soundex_digits = []
    letters = list(name)
    first_letter = letters.pop(0).upper()
    while letters:
        char = letters.pop(0)
        digit = replace_character(char)
        soundex_digits = add_digit_to_soundex_digits(digit, soundex_digits)
    soundex_digits = remove_zeros(soundex_digits)
    soundex_digits = ensure_having_three_numbers(soundex_digits)
    mapping = first_letter + "".join([str(digit) for digit in soundex_digits])
    return mapping


def replace_character(char):
    if char in list("aeiuoywh"):
        return 0
    elif char in list("bfpv"):
        return 1
    elif char in list("cgjkqsxz"):
        return 2
    elif char in list("dt"):
        return 3
    elif char in list("l"):
        return 4
    elif char in list("mn"):
        return 5
    else:  # "r"
        return 6


def add_digit_to_soundex_digits(digit, soundex_digits):
    if len(soundex_digits) == 0:
        soundex_digits.append(digit)
        return soundex_digits
    last_digit = soundex_digits[-1]
    if last_digit != digit:
        soundex_digits.append(digit)
    return soundex_digits


def remove_zeros(soundex_digits):
    return [digit for digit in soundex_digits if digit != 0]


def ensure_having_three_numbers(soundex_digits):
    if len(soundex_digits) < SOUNDEX_NUMBER_LIMIT:
        return add_zeros(soundex_digits)
    return soundex_digits[:SOUNDEX_NUMBER_LIMIT]


def add_zeros(soundex_digits):
    while len(soundex_digits) < SOUNDEX_NUMBER_LIMIT:
        soundex_digits.append(0)
    return soundex_digits


# ----- Unit Tests -----
def test1():
    assert soundex("Jackson") == soundex("Jaxen")
    assert soundex("Jackson") == "J250"


def test2():
    assert soundex("Ropert") == soundex("Rupert")
    assert soundex("Robert") == "R163"


def test3():
    assert soundex("Tymczak") == "T522"


def test4():
    assert soundex("Pfister") == "P123"


def test5():
    assert soundex("Honeyman") == "H555"


if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()
