# ----------------------------
# Author: Tuan Nguyen
# Date: 20190720
#!solutions/68.py
# ----------------------------
"""
On our special chessboard, two bishops attack each other if they share the same diagonal. 
This includes bishops that have another bishop located between them, i.e. bishops can attack through pieces.

You are given N bishops, represented as (row, column) tuples on a M by M chessboard. 
Write a function to count the number of pairs of bishops that attack each other. 
The ordering of the pair doesn't matter: (1, 2) is considered the same as (2, 1).

For example, given M = 5 and the list of bishops:
(0, 0)
(1, 2)
(2, 2)
(4, 0)

The board would look like this:
[b 0 0 0 0]
[0 0 b 0 0]
[0 0 b 0 0]
[0 0 0 0 0]
[b 0 0 0 0]
You should return 2, since bishops 1 and 3 attack each other, as well as bishops 3 and 4.
"""


def printChessboard(M, bishops):
    # input: int M as size of M*M chessboard & list 'bishops' as positions of bishops on chessboard
    # output: print M*M chessboard with 'b' as bishop, '.' as non-bishop
    chessboard = [
        ["." for i in range(M)] for j in range(M)
    ]  # init chessboard w/ all non-bishops
    for bishop in bishops:
        y, x = bishop[0], bishop[1]  # get coordinates of bishop
        chessboard[y][x] = "b"  # mark cell with bishop
    # print chessboard
    for row in chessboard:
        for e in row:
            print(e, end="\t")
        print("\n")


def pairsBishopsAttack(M, bishops):
    # input: int M as size of M*M chessboard & list 'bishops' as positions of bishops on chessboard
    # output: no. pairs of bishops which can attack each other
    noAttackingBishopPairs = 0  # init output=0
    for i in range(len(bishops) - 1):  # check every pair of bishops
        y1, x1 = bishops[i][0], bishops[i][1]  # get coordinates of 1st bishop
        for j in range(i + 1, len(bishops)):
            y2, x2 = (
                bishops[j][0],
                bishops[j][1],
            )  # get coordinates of 2nd bishop
            if abs(x1 - x2) == abs(
                y1 - y2
            ):  # check if 2 bishops are on the same diagonal
                noAttackingBishopPairs += 1  # then increase no. pairs by 1
    return noAttackingBishopPairs


def pairsBishopsAttack_test(M, bishops):
    printChessboard(M, bishops)
    print("No. pairs of attacking bishops:", pairsBishopsAttack(M, bishops))


if __name__ == "__main__":
    pairsBishopsAttack_test(
        M=5, bishops=[(0, 0), (1, 2), (2, 2), (4, 0)]
    )  # return 2
    pairsBishopsAttack_test(
        M=5, bishops=[(0, 4), (1, 2), (2, 2), (4, 0)]
    )  # return 3, b/c bishops can attack through pieces
