# ------------------------
# Author: Tuan Nguyen
# Date created: 20190928
#!solutions/138.py
# ------------------------
"""
Find the minimum number of coins required to make n cents.

You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.

For example, given n = 16, return 3 since we can make it with a 10¢, a 5¢, and a 1¢.
"""
import math

def minCoins(x, availableCoins):
# input: int x as x cents & list of available coins
# output: min no. coins required to make n cents from list of available coins
    availableCoins = sorted(availableCoins, reverse=True)   # sort available coins descendingly
    minCoins = math.inf                                     # initialize min coins for exchange to plus infinitiv from beginning
    n = len(availableCoins)
    for i in range(n):      # find min no. coins by dropping the highest-value coin after each iteration
        val = x                                             # var to temporarily store the input money amount
        noCoins = 0                                         # no. coins for exchage
        for j in range(i, n):       # find min no. coins possible for this this set of available coins
            if val < availableCoins[j]:     # impossible to exchange
                break
            noCoins += val // availableCoins[j]             # max no. coins possible w/ current coin value
            val = val % availableCoins[j]                   # remainer after exchanging
        if noCoins < minCoins:      # update new value of min coins if found a smaller no. coins to exchange
            minCoins = noCoins
    if minCoins == math.inf:
        return "Impossible to exchange"
    return minCoins



def minCoins_test(n, availableCoins, desiredVal):
    print(minCoins(n, availableCoins) == desiredVal)


if __name__ == "__main__":
    minCoins_test(16, [1,5,10,25], 3)
    minCoins_test(31, [1,5,10,25], 3)
    minCoins_test(31, [1,10,25], 4)