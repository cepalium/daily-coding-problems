# -----------------------------
# Author: Tuan Nguyen
# Date created: 20190903
#!solutions/109.py
# -----------------------------
"""
Given an unsigned 8-bit integer, swap its even and odd bits. The 1st and 2nd bit should be swapped, the 3rd and 4th bit should be swapped, and so on.

For example, 10101010 should be 01010101. 11100010 should be 11010001.

Bonus: Can you do this in one line?
"""

def naiveSwap(x):
# input: 8-bit integer
# output: even-odd-bit-swapped 8-bit integer
# method: loop through 8-bit integer and swap its even and odd bits
    x_array = list(str(bin(x)[2:]))
    for i in range(0, len(x_array), 2):
        x_array[i], x_array[i+1] = x_array[i+1], x_array[i] # swap even & odd bit
    swapped_x = ''.join(x_array)  # join list to have string of 8-bit integer after swap
    return int(swapped_x, 2)    # return binary 


def fastSwap(x):
# input: 8-bit integer
# output: even-odd-bit-swapped 8-bit integer
# method: [(x & 10101010) >> 1] | [(x & 01010101) << 1]
    return ((x & 0b10101010) >> 1) | ((x & 0b01010101) << 1)


def swap_test(x):
    print("Naive:\t {:08b} ~> {:08b}".format(x, naiveSwap(x)))
    print("Fast:\t {:08b} ~> {:08b}".format(x, fastSwap(x)))


if __name__ == "__main__":
    swap_test(0b10101010)