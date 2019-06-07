# -----------------------------------
# Author: Tuan Nguyen
# Date: 20190605
#!solutions/23.py
# -----------------------------------
"""
You are given an M by N matrix consisting of booleans that represents a board. 
Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, 
return the minimum number of steps required to reach the end coordinate from the start. 
If there is no possible path, then return null. 
You can move up, left, down, and right. 
You cannot move through walls. You cannot wrap around the edges of the board.

For example, given the following board:
[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]
and start = (3, 0) (bottom left) and end = (0, 0) (top left), 
the minimum number of steps required to reach the end is 7, 
since we would need to go through (1, 2) because there is a wall everywhere else on the second row.
"""

# define boolean variables
f = False
t = True 


def minStepInBoards(board, start, end):
# input: matrix boards of "t"/"f", start & end coordinate [row, column]
# output: min steps from start to end in board
    no_rows = len(board)
    no_cols = len(board[0])
    d = [[no_rows*no_cols for i in range(no_cols)] for j in range(no_rows)] # init matrix distance
    eventList = []
    # initialization
    d[start[0]][start[1]] = 0   # start as 0
    eventList.append(start)
    # loop
    while eventList:
        curPos = eventList.pop(0)   # 1st event in list
        curRow = curPos[0]
        curCol = curPos[1]
        # up
        upRow = curRow - 1
        if ((0<= upRow < no_rows) and (d[curRow][curCol] + 1 < d[upRow][curCol]) and not board[curRow][curCol]):
            d[upRow][curCol] = d[curRow][curCol] + 1
            eventList.append([upRow, curCol])
        # down
        downRow = curRow + 1
        if ((0<= downRow < no_rows) and (d[curRow][curCol] + 1 < d[downRow][curCol]) and not board[curRow][curCol]):
            d[downRow][curCol] = d[curRow][curCol] + 1
            eventList.append([downRow, curCol])
        # left
        leftCol = curCol - 1
        if ((0<= leftCol < no_cols) and (d[curRow][curCol] + 1 < d[curRow][leftCol]) and not board[curRow][curCol]):
            d[curRow][leftCol] = d[curRow][curCol] + 1
            eventList.append([curRow, leftCol])
        # right
        rightCol = curCol + 1
        if ((0<= rightCol < no_cols) and (d[curRow][curCol] + 1 < d[curRow][rightCol]) and not board[curRow][curCol]):
            d[curRow][rightCol] = d[curRow][curCol] + 1
            eventList.append([curRow, rightCol])

    if d[end[0]][end[1]] < no_rows*no_cols:
        return d[end[0]][end[1]]
    return "null"


def minStepInBoards_test(board, start, end):
    for line in board:
        print(line)
    print("Start: ", start, "-> End: ", end)
    print("Min steps: ", minStepInBoards(board, start, end))


if __name__ == "__main__":
    minStepInBoards_test([[f, f, f, f], [t, t, f, t], [f, f, f, f], [f, f, f, f]], (3,0), (0,0))   # return 7
    minStepInBoards_test([[f, f, f, f], [t, t, t, t], [f, f, f, f], [f, f, f, f]], (3,0), (0,0))   # return "null", row[1] is all blocked