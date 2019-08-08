# ---------------------------
# Author: Tuan Nguyen
# Date: 20190807
#!solutions/84.py
# ---------------------------
"""
Given a matrix of 1s and 0s, return the number of "islands" in the matrix. 
A 1 represents land and 0 represents water, 
so an island is a group of 1s that are neighboring whose perimeter is surrounded by water.

For example, this matrix has 4 islands.
1 0 0 0 0
0 0 1 1 0
0 1 1 0 0
0 0 0 0 0
1 1 0 0 1
1 1 0 0 1
"""

import random


def checkAround(x, y, islands):
# input: 2D matrix
# output: 0 if
    rows = len(islands)
    cols = len(islands[0])
    for i in range(y-1, y+2):
        for j in range(x-1, x+2):
            if (0 <= i < rows) and (0 <= j < cols) and islands[i][j]:
                return islands[i][j]
    return 0


def listNeighborCells(x, y, matrix):
# input:
# output:
    #
    rows = len(matrix)
    cols = len(matrix[0])
    #
    neighbors = []
    #
    for i in range(y-1, y+2):
        for j in range(x-1, x+2):
            if (0 <= i < rows) and (0 <= j < cols) and matrix[i][j]:
                neighbors.append((j, i))
    return neighbors


def numberIslands(matrix):
# input:
# output:
    #
    rows = len(matrix)
    cols = len(matrix[0])
    #
    islands = [[0 for i in range(cols)] for j in range(rows)] 
    islandsNr = 0
    #
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                continue
            if islands[i][j] != 0:
                continue
            # check = checkAround(j, i, islands)
            # if check:
            #     islands[i][j] = check
            # else: 
            #     islandsNr += 1
            #     islands[i][j] = islandsNr
            """
            not finish
            """
            islandsNr += 1
            islands[i][j] = islandsNr
            neighbors = listNeighborCells(j, i, matrix)
            for coord in neighbors:
                x = coord[0]
                y = coord[1]
                islands[y][x] = islandsNr

    return islandsNr, islands


def numberIslands_test(matrix):
    islandNr = numberIslands(matrix)[0]
    islandMap = numberIslands(matrix)[1]

    print("Input matrix:")
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=' ')
        print("\n")

    print("No. islands: {}".format(islandNr))
    print("Island map:")
    for i in range(len(islandMap)):
        for j in range(len(islandMap[0])):
            print(islandMap[i][j], end=' ')
        print("\n")


if __name__ == "__main__":
    numberIslands_test(matrix=  [[1, 0, 0, 0, 0],
                                [0, 0, 1, 1, 0],
                                [0, 1, 1, 0, 0],
                                [0, 0, 0, 0, 0],
                                [1, 1, 0, 0, 1],
                                [1, 1, 0, 0, 1]])   # return 4
    
    side = 7
    numberIslands_test(matrix= [[random.randint(0,1) for i in range(side)] for j in range(side)])