# ---------------------------
# Author: Tuan Nguyen
# Date created: 20200603
#!384.py
# ---------------------------
"""
You are given an array of integers representing coin denominations and a total amount of money. 
Write a function to compute the fewest number of coins needed to make up that amount. 
If it is not possible to make that amount, return null.

For example, given an array of [1, 5, 10] and an amount 56, 
return 7 since we can use 5 dimes, 1 nickel, and 1 penny.

Given an array of [5, 8] and an amount 15, return 3 since we can use 5 5-cent coins.
"""


def least_coins(coins, amount):
    """solved with dynamic programming: Knapsack problem"""
    if not coins or not amount:
        return None
    n = len(coins)
    values = [1 for i in range(n)]
    K = [None for i in range(amount + 1)]
    K[0] = 0  # base case
    # Bellman's equation:
    # K[w] = min{K[w - coins[i]] + values[i] | i < n & K[w - coins[i]]}
    for w in range(1, amount + 1):
        k_w = []
        for i in range(n):
            if w >= coins[i] and K[w - coins[i]] != None:
                k_w.append(K[w - coins[i]] + values[i])
        if k_w:
            K[w] = min(k_w)
    return K[amount]


def test1():
    assert least_coins([1, 5, 10], 56) == 7


def test2():
    assert least_coins([5, 8], 15) == 3


def test3():
    assert least_coins([5, 10], 56) == None


if __name__ == "__main__":
    test1()
    test2()
    test3()
