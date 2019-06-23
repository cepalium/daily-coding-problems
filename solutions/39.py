# --------------------------------------
# Author: Tuan Nguyen
# Date: 20190621
#!solutions/39.py
# --------------------------------------
"""
Conway's Game of Life takes place on an infinite two-dimensional board of square cells. 
Each cell is either dead or alive, and at each tick, the following rules apply:

Any live cell with less than two live neighbours dies.
Any live cell with two or three live neighbours remains living.
Any live cell with more than three live neighbours dies.
Any dead cell with exactly three live neighbours becomes a live cell.
A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent.

Implement Conway's Game of Life. 
It should be able to be initialized with a starting list of live cell coordinates 
and the number of steps it should run for. 
Once initialized, it should print out the board state at each step. 
Since it's an infinite board, print out only the relevant coordinates, 
i.e. from the top-leftmost live cell to bottom-rightmost live cell.

You can represent a live cell with an asterisk (*) and a dead cell with a dot (.).
"""

class ConwayGameOfLife():
# Class: Conway's Game of Life
    def __init__(self, liveCells: [], iterations: int):
        self.liveCells = liveCells
        self.iterations = iterations


    def getCoords(self):
    # input:
    # output:
        x_coords = [cell[0] for cell in self.liveCells]
        y_coords = [cell[1] for cell in self.liveCells]
        most_left = min(x_coords) - 1
        most_right = max(x_coords) + 1
        most_down = min(y_coords) - 1
        most_up = max(y_coords) + 1

        return most_left, most_right, most_down, most_up

    def countLiveNeighbors(self, x, y):
    # input:
    # output:
        liveNeighbors = 0
        for i in range(x-1, x+2):   # x-axis from x-1 to x+1
            for j in range(y-1, y+2):   # y-axis from y-1 to y+1
                if (i==x) and (j==y):   # not check the input cell
                    continue
                if [i, j] in self.liveCells:
                    liveNeighbors += 1
        return liveNeighbors


    def updateCells(self):
    # input: list liveCells of list [int x, int y] as live cells
    # output: next state of liveCells
        newLiveCells = []

        most_left, most_right, most_down, most_up = self.getCoords()

        for i in range(most_left, most_right+1):
            for j in range(most_down, most_up+1):
                liveNeighbors = self.countLiveNeighbors(i, j)
                if ([i,j] in self.liveCells) and (2 <= liveNeighbors <= 3):
                    newLiveCells.append([i,j])
                if ([i,j] not in self.liveCells) and (liveNeighbors==3):
                    newLiveCells.append([i,j])

        return newLiveCells


    def printCells(self):
    # input: list liveCells of list [int x, int y] as live cells
    # output: print liveCells as Conway's Game of Life
        most_left, most_right, most_down, most_up = self.getCoords()

        for i in range(most_left, most_right+1):
            for j in range(most_down, most_up+1):
                if [i,j] in self.liveCells:
                    print("*", end=' ')
                else:
                    print(".", end=' ')
            print("\n")
                


    def play(self):
    # task: implementation of Conway's Game of Life
        print("Initilization =====")
        self.printCells()
        for i in range(self.iterations):
            self.liveCells = self.updateCells()
            print("Iteration: ", i+1, " =====")
            self.printCells()


def gameOfLife_test(liveCells, iterations):
    gameOfLife = ConwayGameOfLife(liveCells=liveCells, iterations=iterations)
    gameOfLife.play()


if __name__ == "__main__":
    gameOfLife_test(liveCells=[[1,1],[1,2],[2,1],[3,4],[4,3],[4,4]], iterations=3)  # beacon
    gameOfLife_test(liveCells=[[2,1],[2,2],[2,3]], iterations=3)    # blinker
    gameOfLife_test(liveCells=[[2,2],[2,3],[2,4],[3,1],[3,2],[3,3]], iterations=3) # toad