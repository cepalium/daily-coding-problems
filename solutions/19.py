# -----------------------------
# Author: Tuan Nguyen
# Date: 2090601
#!solutions/19.py
# -----------------------------
"""
A builder is looking to build a row of N houses that can be of K different colors. 
He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, 
return the minimum cost which achieves this goal.
"""


def minCostPaintHouse(houseCost):
# input: size-n*k matrix houseCost, n rows = n houses, k columns = k colors
# output: min cost to paint all houses w/ no same color for 2 neighboring houses
# method: dynamic programming
    n = len(houseCost)      # no. houses
    k = len(houseCost[0])   # no. colors
    cost = [[0 for i in range(k)] for j in range(n)]    # init cost matrix 
    # base case
    cost[0] = houseCost[0]
    # iteration
    for i in range(1, n): # from 2nd house (index 1) to n-th house (index n-1) 
        for j in range(k):  # from color 1 (index 0) to color k (index k-1)
            # Bellman's equation
            cost[i][j] = houseCost[i][j] + min(cost[i-1][:j] + cost[i-1][j+1:])
    return min(cost[n-1])   # min of last row in matrix cost


def minCostPaintHouse_test(houseCost):
    print(houseCost, minCostPaintHouse(houseCost))


if __name__ == "__main__":
    minCostPaintHouse_test([[1,2,3],[4,5,6],[7,8,9]])   # return 13
    minCostPaintHouse_test([[3,5,1],[7,8,2],[1,5,6]])   # return 6