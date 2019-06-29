# ---------------------------------
# Author: Tuan Nguyen
# Date: 20190629
#!solutions/47.py
# ---------------------------------
"""
Given a array of numbers representing the stock prices of a company in chronological order, 
write a function that calculates the maximum profit you could have made from buying and selling that stock once. 
You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, 
since you could buy the stock at 5 dollars and sell it at 10 dollars.
"""

def maxProfitFromStocks(stocks):
# input: list 'stocks' of int as stock prices
# output: max profit from buying first and selling that stock later
    maxProfit = stocks[1] - stocks[0]   # init maxProfit
    for i in range(len(stocks)-1):
        buy = stocks[i]
        for j in range(i+1, len(stocks)):
            sell = stocks[j]
            if sell - buy > maxProfit:  # update maxProfit
                maxProfit = sell - buy
    return maxProfit


def maxProfitFromStocks_test(stocks):
    print(stocks, "max profit:", maxProfitFromStocks(stocks))


if __name__ == "__main__":
    maxProfitFromStocks_test([9, 11, 8, 5, 7, 10])  # return 5