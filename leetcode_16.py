# 37. Sudoku Solver
# Write a program to solve a Sudoku puzzle by filling the empty cells.
# A sudoku solution must satisfy all the following rules:
# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        pass


# IDEA:
# for all empty units create a list of possible values based on boxes, rows and columns
# when one is length one (only one possibility) then set its value on the board and update the same box, row and column
# remove the previous value from all the previous lists of possible values
# repeat0


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]


# check row by checking individual list: board[0] = 0th row
# check column by using a list compression: [row[0] for row in board] = 0th column
# check box by hard-coding boxes


box_0 = [n for arr in [r[0:3] for r in board[0:3]] for n in arr]
box_1 = [n for arr in [r[3:6] for r in board[0:3]] for n in arr]
box_2 = [n for arr in [r[6:9] for r in board[0:3]] for n in arr]
box_3 = [n for arr in [r[0:3] for r in board[3:6]] for n in arr]
box_4 = [n for arr in [r[3:6] for r in board[3:6]] for n in arr]
box_5 = [n for arr in [r[6:9] for r in board[3:6]] for n in arr]
box_6 = [n for arr in [r[0:3] for r in board[6:9]] for n in arr]
box_7 = [n for arr in [r[3:6] for r in board[6:9]] for n in arr]
box_8 = [n for arr in [r[6:9] for r in board[6:9]] for n in arr]


# arr = [[[1, 2, 3]]]
# print([i for sub_out in arr for sub_in in sub_out for i in sub_in])


unit_values = [[] for _ in range(9**2)]
counter = 0
for i in range(len(board)):
    for j in range(len(board[i])):
        unit_values[counter] = [board[i][j]]
        counter += 1
print(f"{unit_values.count(['.'])} missing values.")


# print row 2  (starts from 0)
print(unit_values[9*2: 9*(2+1)])

# print col 4
print(unit_values[4::9])


print()


# print box 3
# print(
#     unit_values[9*3 + (3 % 3)*3: 9*3 + (3 % 3)*3 + 3] +
#     unit_values[9*4 + (3 % 3)*3: 9*4 + (3 % 3)*3 + 3] +
#     unit_values[9*5 + (3 % 3)*3: 9*5 + (3 % 3)*3 + 3]
# )
# print box 4
print(
    unit_values[9*int(4/3)*3 + (4 % 3)*3: 9*3 + (4 % 3)*3 + 3] +
    unit_values[9*int(4/3)*(3+1) + (4 % 3)*3: 9*4 + (4 % 3)*3 + 3] +
    unit_values[9*int(4/3)*(3+2) + (4 % 3)*3: 9*5 + (4 % 3)*3 + 3]
)


def get_row(n: int):
    assert 0 <= n <= 9
    return unit_values[9*n: 9*(n+1)]


def get_col(n: int):
    assert 0 <= n <= 9
    return unit_values[n::9]


def get_box(n: int):
    assert 0 <= n <= 8
    return (
            unit_values[3*9*int(n/3) + (n % 3)*3: 3*9*int(n/3) + (n % 3)*3 + 3] +
            unit_values[3*9*int(n/3) + 9 + (n % 3)*3: 3*9*int(n/3) + 9 + (n % 3)*3 + 3] +
            unit_values[3*9*int(n/3) + 18 + (n % 3)*3: 3*9*int(n/3) + 18 + (n % 3)*3 + 3]
            )


# given a number of unit in the board [0, 81], find a way to determine its corresponding row, col and box
# for row it's div 9: int(n/9)
# for column it's the module: n%9
# for box is int(row_80/3)*3 + int(col_80/3)

