# ---------------------------------
# Author: Tuan Nguyen
# Date: 20190721
#!solutions/69.py
# ---------------------------------
"""
Given a list of integers, return the largest product that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

You can assume the list has at least three integers.
"""


def largestThreeProduct(li):
    # input: list of ints 'li'
    # output: largest product from 3 ints
    # running time: O(n*logn)
    # trivial case
    if len(li) == 3:
        return li[0] * li[1] * li[2]
    # sort and pick important values
    li.sort()  # running time: O(n*logn)
    maxInt = li[-1]
    secondMaxInt = li[-2]
    thirdMaxInt = li[-3]
    minInt = li[0]
    secondMinInt = li[1]
    # compare 2 possibly largest products of 3 ints
    product_1 = maxInt * secondMaxInt * thirdMaxInt  # case 1
    product_2 = minInt * secondMinInt * maxInt  # case 2
    if product_1 >= product_2:
        return product_1
    return product_2


def largestThreeProduct_test(li):
    print(li, "~> largest product:", largestThreeProduct(li))


if __name__ == "__main__":
    largestThreeProduct_test([-10, -10, 5, 2])  # return 500
    largestThreeProduct_test([-10, -10, 2])  # return 200
    largestThreeProduct_test([-10, -10, -5, -2, -15])  # return -100
    largestThreeProduct_test([10, 15, 5, 2])  # return 750
