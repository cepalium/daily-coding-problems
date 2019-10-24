# -----------------------------------
# Author: Tuan Nguyen
# Date: 20190717
#!solutions/65.py
# -----------------------------------
"""
Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

For example, given the following matrix:
[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]

You should print out the following:
1
2
3
4
5
10
15
20
19
18
17
16
11
6
7
8
9
14
13
12
"""

def nextMove(matrix, cellState, curX, curY, curDir):
# input: N*M matrix, matrix state "visited", list 'curPos' [x,y] & string 'direction' (left, right, down, up)
# output: nextX, nextY, nextDir
    # matrix metadata
    n = len(matrix) # no. rows
    m = len(matrix[0])  # no. cols
    # init ~> temporary values
    nextDir = curDir
    nextX = curX
    nextY = curY
    # change direction according to clockwise
    # when: current cell is at border or its next cell (following the current direction) was visited  
    if (curDir == "left") and ((curX == 0) or cellState[curY][curX-1]): # change left to up
        nextDir = "up"
    if (curDir == "right") and ((curX == m-1) or cellState[curY][curX+1]):  # change right to down
        nextDir = "down"
    if (curDir == "down") and ((curY == n-1) or cellState[curY+1][curX]):   # change down to left
        nextDir = "left"
    if (curDir == "up") and ((curY == 0) or cellState[curY-1][curX]):   # change up to right
        nextDir = "right"
    # calculate next position (x, y)
    if nextDir == "left":
        nextX = curX - 1
        nextY = curY
    if nextDir == "right":
        nextX = curX + 1
        nextY = curY
    if nextDir == "down":
        nextX = curX
        nextY = curY + 1
    if nextDir == "up":
        nextX = curX
        nextY = curY - 1
    # print('current:', curX, curY, curDir, '~> next:', nextX, nextY, nextDir)
    return nextX, nextY, nextDir
    

def printClockwiseSpiral(matrix):
# input: N*M matrix
# output: print matrix in a clockwise spiral
    # matrix metadata
    n = len(matrix)
    m = len(matrix[0])
    # init
    x = 0   # starting x ~> x: horizontal axis
    y = 0   # starting y ~> y: vertical axis
    direction = "right" # starting direction: right
    counter = 0 # var to stop when print all cells of matrix
    state = [[False for i in range(m)] for j in range(n)]   # matrix to store cell state ~> True if visited, False if not visited
    # loop
    while counter < n*m:
        print(matrix[y][x]) # print cell
        state[y][x] = True  # cell state ~> visited
        counter += 1    # no. visited cells
        if counter == n*m:  # finish printing all cells of matrix 
            break
        x, y, direction = nextMove(matrix, state, x, y, direction)  # get next info of x, y, direction


def printClockwiseSpiral_test(matrix):
    for row in matrix:
        print(row)
    printClockwiseSpiral(matrix)


if __name__ == "__main__":
    printClockwiseSpiral_test([ [1,  2,  3,  4,  5],
                                [6,  7,  8,  9,  10],
                                [11, 12, 13, 14, 15],
                                [16, 17, 18, 19, 20]])