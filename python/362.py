# ----------------------------
# Author: Tuan Nguyen
# Date created: 20200510
#!362.py
# ----------------------------
"""
A strobogrammatic number is a positive number that appears the same after being rotated 180 degrees. 
For example, 16891 is strobogrammatic.

Create a program that finds all strobogrammatic numbers with N digits.
"""


def find_strobogramatic_numbers_N_digits(N):
    if N == 0:  # trivial cases
        return []
    if N == 1:
        return [0, 1, 8]
    results = []
    string_strobogramatic_numbers = (
        find_string_strobogramatic_numbers_N_digits(N)
    )
    for n_str in string_strobogramatic_numbers:
        if is_valid_string_strobogramatic_number(n_str, N):
            results.append(int(n_str))
    return results


def find_string_strobogramatic_numbers_N_digits(N):
    if N == 0:  # trivial cases
        return [""]
    if N == 1:
        return ["0", "1", "8"]
    # else:
    results = []
    middles = find_string_strobogramatic_numbers_N_digits(
        N - 2
    )  # -2 to add strobo digits at 2 ends later
    for m in middles:
        results.append("0" + m + "0")
        results.append("1" + m + "1")
        results.append("8" + m + "8")
        results.append("6" + m + "9")
        results.append("9" + m + "6")
    return results


def is_valid_string_strobogramatic_number(n_str, N):
    if not len(n_str):  # blank string
        return False
    n_without_0_both_ends = n_str.strip("0")
    if len(n_without_0_both_ends) == N:
        return True
    return False  # the string after converting into integer will have less digits than N


def test0():
    assert find_strobogramatic_numbers_N_digits(0) == []


def test1():
    assert find_strobogramatic_numbers_N_digits(1) == [0, 1, 8]


def test2():
    assert find_strobogramatic_numbers_N_digits(2) == [11, 88, 69, 96]


def test3():
    assert find_strobogramatic_numbers_N_digits(3) == [
        101,
        808,
        609,
        906,
        111,
        818,
        619,
        916,
        181,
        888,
        689,
        986,
    ]


def test4():
    assert len(find_strobogramatic_numbers_N_digits(4)) == 20


if __name__ == "__main__":
    test0()
    test1()
    test2()
    test3()
    test4()
