# -----------------------
# Author: Tuan Nguyen
# Date created: 20191010
#!solutions/148.py
# -----------------------
"""
Gray code is a binary code where each successive value differ in only one bit, as well as when wrapping around. 
Gray code is common in hardware so that we don't see temporary spurious values during transitions.

Given a number of bits n, generate a possible gray code for it.

For example, for n = 2, one gray code would be [00, 01, 11, 10].
"""


def grayCodeGenerator(n):
    # input: int n as number of bits
    # output: list of gray codes for n bits
    if n <= 0:
        return []
    elif n == 1:
        return ["0", "1"]
    else:
        L1 = grayCodeGenerator(n - 1)
        L2 = reversed(L1)
        L1 = ["0" + e for e in L1]
        L2 = ["1" + e for e in L2]
        return L1 + L2


def grayCodeGenerator_test(n, desiredVal):
    print(grayCodeGenerator(n) == desiredVal)


if __name__ == "__main__":
    grayCodeGenerator_test(n=0, desiredVal=[])
    grayCodeGenerator_test(n=1, desiredVal=["0", "1"])
    grayCodeGenerator_test(n=2, desiredVal=["00", "01", "11", "10"])
    grayCodeGenerator_test(
        n=3,
        desiredVal=["000", "001", "011", "010", "110", "111", "101", "100"],
    )
    grayCodeGenerator_test(
        n=4,
        desiredVal=[
            "0000",
            "0001",
            "0011",
            "0010",
            "0110",
            "0111",
            "0101",
            "0100",
            "1100",
            "1101",
            "1111",
            "1110",
            "1010",
            "1011",
            "1001",
            "1000",
        ],
    )
