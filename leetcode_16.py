# 37. Sudoku Solver
# Write a program to solve a Sudoku puzzle by filling the empty cells.
# A sudoku solution must satisfy all the following rules:
# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.
from typing import List


# class Solution:
#     def solveSudoku(self, board: List[List[str]]) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """
#         unit_values = []
#         for i in range(len(board)):
#             for j in range(len(board[i])):
#                 unit_values.append(board[i][j])
#         MAX_ITER = 500
#         numbers = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
#         for _ in range(MAX_ITER):
#
#             missing_dict = {}
#             for idx in range(len(unit_values)):
#                 if unit_values[idx] == '.':
#                     row = int(idx / 9)
#                     col = idx % 9
#                     box = int(row / 3) * 3 + int(col / 3)
#                     values = set(self.get_row(row, unit_values)).union(set(self.get_col(col, unit_values))).union(
#                         set(self.get_box(box, unit_values)))
#                     values.remove('.')
#                     missing_dict[idx] = numbers.difference(values)
#             if len(missing_dict) == 0:
#                 boardy = []
#                 chunk = 9
#                 for idx in range(0, len(unit_values), chunk):
#                     boardy.append(unit_values[idx: idx + chunk])
#                 for idx in range(len(board)):
#                     board[idx] = boardy[idx]
#                 break
#             n_missing_values = unit_values.count('.')
#             for idx, missings in missing_dict.items():
#                 if len(missings) == 1:
#                     v = missings.pop()
#                     unit_values[idx] = v
#             if unit_values.count('.') == n_missing_values:
#
#                 min_key = min(missing_dict, key=lambda k: len(missing_dict[k]))
#                 min_set = missing_dict[min_key]
#                 done = False
#
#                 for v in min_set:
#
#                     unit_values_copy = unit_values[:]
#                     unit_values_copy[min_key] = v
#
#                     for _ in range(MAX_ITER):
#
#                         missing_dict = {}
#
#                         for idx in range(len(unit_values_copy)):
#                             if unit_values_copy[idx] == '.':
#                                 row = int(idx / 9)
#                                 col = idx % 9
#                                 box = int(row / 3) * 3 + int(col / 3)
#                                 values = set(self.get_row(row, unit_values_copy)).union(
#                                     set(self.get_col(col, unit_values_copy))).union(
#                                     set(self.get_box(box, unit_values_copy)))
#                                 values.remove('.')
#                                 missing_dict[idx] = numbers.difference(values)
#
#                         if len(missing_dict) == 0:
#                             done = True
#                             boardy = []
#                             chunk = 9
#                             for idx in range(0, len(unit_values_copy), chunk):
#                                 boardy.append(unit_values_copy[idx: idx + chunk])
#                             for idx in range(len(board)):
#                                 board[idx] = boardy[idx]
#                             break
#
#                         n_missing_values = unit_values_copy.count('.')
#                         for idx, missings in missing_dict.items():
#                             if len(missings) == 1:
#                                 v = missings.pop()
#                                 unit_values_copy[idx] = v
#                         if unit_values_copy.count('.') == n_missing_values:
#                             break
#                     if done:
#                         break
#
#     def get_row(self, n: int, b):
#         assert 0 <= n <= 9
#         return b[9 * n: 9 * (n + 1)]
#
#     def get_col(self, n: int, b):
#         assert 0 <= n <= 9
#         return b[n::9]
#
#     def get_box(self, n: int, b):
#         assert 0 <= n <= 8
#         return (
#                 b[3 * 9 * int(n / 3) + (n % 3) * 3: 3 * 9 * int(n / 3) + (n % 3) * 3 + 3] +
#                 b[3 * 9 * int(n / 3) + 9 + (n % 3) * 3: 3 * 9 * int(n / 3) + 9 + (n % 3) * 3 + 3] +
#                 b[3 * 9 * int(n / 3) + 18 + (n % 3) * 3: 3 * 9 * int(n / 3) + 18 + (n % 3) * 3 + 3]
#         )
#
#     def create_board_from_list(self, b):
#         boardy = []
#         chunk = 9
#         for idx in range(0, len(b), chunk):
#             boardy.append(b[idx: idx + chunk])
#         board = boardy


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        unit_values = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                unit_values.append(board[i][j])
        self.go_through_recursive(board, unit_values)

    def get_row(self, n: int, b):
        assert 0 <= n <= 9
        return set(b[9 * n: 9 * (n + 1)])

    def get_col(self, n: int, b):
        assert 0 <= n <= 9
        return set(b[n::9])

    def get_box(self, n: int, b):
        assert 0 <= n <= 8
        return set(
                b[3 * 9 * int(n / 3) + (n % 3) * 3: 3 * 9 * int(n / 3) + (n % 3) * 3 + 3] +
                b[3 * 9 * int(n / 3) + 9 + (n % 3) * 3: 3 * 9 * int(n / 3) + 9 + (n % 3) * 3 + 3] +
                b[3 * 9 * int(n / 3) + 18 + (n % 3) * 3: 3 * 9 * int(n / 3) + 18 + (n % 3) * 3 + 3]
        )

    def go_through_recursive(self, board, b, d=False):
        """
        :param board: sudoku board as matrix where each row is a line
        :param b: sudoku board as a single long list
        """
        numbers = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

        for _ in range(500):

            if d:
                return True

            missing_dict = {}  # populate missing_dict
            for idx in range(len(b)):
                if b[idx] == '.':
                    row = int(idx / 9)
                    col = idx % 9
                    box = int(row / 3) * 3 + int(col / 3)
                    values = self.get_row(row, b).union(self.get_col(col, b)).union(self.get_box(box, b))
                    values.remove('.')
                    missing_dict[idx] = numbers.difference(values)
                    if len(missing_dict[idx]) == 0:  # if an empty space has no possible value we failed
                        del b
                        return False

            # store assured values
            old_count = b.count('.')
            for idx, missings in missing_dict.items():
                if len(missings) == 1:

                    row = int(idx / 9)
                    col = idx % 9
                    box = int(row / 3) * 3 + int(col / 3)
                    values = self.get_row(row, b).union(self.get_col(col, b)).union(self.get_box(box, b))
                    values.remove('.')  # some of these values are [1, 9]
                    missing_one = numbers.difference(values)
                    if len(missing_one) == 0:
                        print(values)
                    # print(values)
                    v = missings.pop()
                    print(v)
                    # if v != numbers.difference(values).pop():
                    #     return False

                    # v = missings.pop()
                    b[idx] = v

            if b.count('.') == 0:  # check if complete
                self.create_board_from_list(board, b)
                return True

            if b.count('.') == old_count:  # if no progress has been made
                for idx, s in missing_dict.items():  # iterate through the dictionary
                    for number in s:  # create a new board and store indecisive value then recur
                        if d:
                            return True
                        bb = b[:]
                        bb[idx] = number
                        d = self.go_through_recursive(board, bb)

    def create_board_from_list(self, board, b):
        boardy = []
        chunk = 9
        for idx in range(0, len(b), chunk):
            boardy.append(b[idx: idx + chunk])
        for idx in range(len(board)):
            board[idx] = boardy[idx]
        print('done')


# IDEA:
# for all empty units create a list of possible values based on boxes, rows and columns
# when one is length one (only one possibility) then set its value on the board and update the same box, row and column
# remove the previous value from all the previous lists of possible values
# repeat0


def create_board_from_list(b):
    boardy = []
    chunk = 9
    for idx in range(0, len(b), chunk):
        boardy.append(b[idx: idx + chunk])
    for idx in range(len(board)):
        board[idx] = boardy[idx]
    print('complete.')


# board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
#          ["6", ".", ".", "1", "9", "5", ".", ".", "."],
#          [".", "9", "8", ".", ".", ".", ".", "6", "."],
#          ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
#          ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
#          ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#          [".", "6", ".", ".", ".", ".", "2", "8", "."],
#          [".", ".", ".", "4", "1", "9", ".", ".", "5"],
#          [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

# board = [[".", ".", "9", "7", "4", "8", ".", ".", "."],
#          ["7", ".", ".", ".", ".", ".", ".", ".", "."],
#          [".", "2", ".", "1", ".", "9", ".", ".", "."],
#          [".", ".", "7", ".", ".", ".", "2", "4", "."],
#          [".", "6", "4", ".", "1", ".", "5", "9", "."],
#          [".", "9", "8", ".", ".", ".", "3", ".", "."],
#          [".", ".", ".", "8", ".", "3", ".", "2", "."],
#          [".", ".", ".", ".", ".", ".", ".", ".", "6"],
#          [".", ".", ".", "2", "7", "5", "9", ".", "."]]


board = [[".", ".", ".", "2", ".", ".", ".", "6", "3"],
         ["3", ".", ".", ".", ".", "5", "4", ".", "1"],
         [".", ".", "1", ".", ".", "3", "9", "8", "."],
         [".", ".", ".", ".", ".", ".", ".", "9", "."],
         [".", ".", ".", "5", "3", "8", ".", ".", "."],
         [".", "3", ".", ".", ".", ".", ".", ".", "."],
         [".", "2", "6", "3", ".", ".", "5", ".", "."],
         ["5", ".", "3", "7", ".", ".", ".", ".", "8"],
         ["4", "7", ".", ".", ".", "1", ".", ".", "."]]

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


# unit_values = [[] for _ in range(9**2)]
# unit_values = [_ for _ in range(9 ** 2)]
# counter = 0
# for i in range(len(board)):
#     for j in range(len(board[i])):
#         # unit_values[counter] = [board[i][j]]
#         unit_values[counter] = board[i][j]
#         counter += 1
# # print(f"{unit_values.count(['.'])} missing values.")
# print(f"{unit_values.count('.')} missing values.")
#
# # print row 2  (starts from 0)
# print(unit_values[9 * 2: 9 * (2 + 1)])
#
# # print col 4
# print(unit_values[4::9])
#
# print()

# print box 3
# print(
#     unit_values[9*3 + (3 % 3)*3: 9*3 + (3 % 3)*3 + 3] +
#     unit_values[9*4 + (3 % 3)*3: 9*4 + (3 % 3)*3 + 3] +
#     unit_values[9*5 + (3 % 3)*3: 9*5 + (3 % 3)*3 + 3]
# )
# # print box 4
# print(
#     unit_values[9 * int(4 / 3) * 3 + (4 % 3) * 3: 9 * 3 + (4 % 3) * 3 + 3] +
#     unit_values[9 * int(4 / 3) * (3 + 1) + (4 % 3) * 3: 9 * 4 + (4 % 3) * 3 + 3] +
#     unit_values[9 * int(4 / 3) * (3 + 2) + (4 % 3) * 3: 9 * 5 + (4 % 3) * 3 + 3]
# )


# def get_row(n: int):
#     assert 0 <= n <= 9
#     return unit_values[9*n: 9*(n+1)]
#
#
# def get_col(n: int):
#     assert 0 <= n <= 9
#     return unit_values[n::9]
#
#
# def get_box(n: int):
#     assert 0 <= n <= 8
#     return (
#             unit_values[3*9*int(n/3) + (n % 3)*3: 3*9*int(n/3) + (n % 3)*3 + 3] +
#             unit_values[3*9*int(n/3) + 9 + (n % 3)*3: 3*9*int(n/3) + 9 + (n % 3)*3 + 3] +
#             unit_values[3*9*int(n/3) + 18 + (n % 3)*3: 3*9*int(n/3) + 18 + (n % 3)*3 + 3]
#             )


def get_row(n: int, b):
    assert 0 <= n <= 9
    return b[9 * n: 9 * (n + 1)]


def get_col(n: int, b):
    assert 0 <= n <= 9
    return b[n::9]


def get_box(n: int, b):
    assert 0 <= n <= 8
    return (
            b[3 * 9 * int(n / 3) + (n % 3) * 3: 3 * 9 * int(n / 3) + (n % 3) * 3 + 3] +
            b[3 * 9 * int(n / 3) + 9 + (n % 3) * 3: 3 * 9 * int(n / 3) + 9 + (n % 3) * 3 + 3] +
            b[3 * 9 * int(n / 3) + 18 + (n % 3) * 3: 3 * 9 * int(n / 3) + 18 + (n % 3) * 3 + 3]
    )


# given a number of unit in the board [0, 81], find a way to determine its corresponding row, col and box
# for row it's div 9: int(n/9)
# for column it's the module: n%9
# for box is int(row/3)*3 + int(col/3)


# numbers = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
# position = 3
# u_row = int(position/9)
# u_col = position % 9
# u_box = int(u_row/3) * 3 + int(u_col/3)


# values = set(get_row(u_row)).union(set(get_col(u_col))).union(set(get_box(u_box)))
# values.remove('.')
# possible_values = numbers.difference(values)


MAX_ITER = 500
numbers = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}


# for _ in range(500):
#
#     missing_dict = {}
#
#     for idx in range(len(unit_values)):
#         if unit_values[idx] == '.':
#             row = int(idx / 9)
#             col = idx % 9
#             box = int(row / 3) * 3 + int(col / 3)
#             values = set(get_row(row, unit_values)).union(set(get_col(col, unit_values))).union(
#                 set(get_box(box, unit_values)))
#             values.remove('.')
#             missing_dict[idx] = numbers.difference(values)
#
#     if len(missing_dict) == 0:
#         create_board_from_list(unit_values)
#         break
#
#     n_missing_values = unit_values.count('.')
#     for idx, missings in missing_dict.items():
#         if len(missings) == 1:
#             v = missings.pop()
#             unit_values[idx] = v
#
#     if unit_values.count('.') == n_missing_values:
#         min_key = min(missing_dict, key=lambda k: len(missing_dict[k]))
#         min_set = missing_dict[min_key]
#         for v in min_set:
#             unit_values_copy = unit_values[:]
#             unit_values_copy[min_key] = v
#             done = False
#             for _ in range(MAX_ITER):
#                 missing_dict = {}
#                 for idx in range(len(unit_values_copy)):
#                     if unit_values_copy[idx] == '.':
#                         row = int(idx / 9)
#                         col = idx % 9
#                         box = int(row / 3) * 3 + int(col / 3)
#                         values = set(get_row(row, unit_values_copy)).union(set(get_col(col, unit_values_copy))).union(
#                             set(get_box(box, unit_values_copy)))
#                         values.remove('.')
#                         missing_dict[idx] = numbers.difference(values)
#                 if len(missing_dict) == 0:
#                     create_board_from_list(unit_values_copy)
#                     done = True
#                     break
#                 n_missing_values = unit_values_copy.count('.')
#                 for idx, missings in missing_dict.items():
#                     if len(missings) == 1:
#                         v = missings.pop()
#                         unit_values_copy[idx] = v
#                 if unit_values_copy.count('.') == n_missing_values:
#                     print('Huston we have a problem.')
#                     break
#             if done:
#                 break


# print(f"{unit_values.count('.')} missing values.")
# indices_to_delete = []
# for idx, v in missing_dict.items():
#     if len(v) == 0:
#         indices_to_delete.append(idx)
#     print(f'{idx} : {v}')
# for i in indices_to_delete:
#     del missing_dict[i]


# print(unit_values_copy.count('.'))


def go_through_recursive(b):
    for _ in range(MAX_ITER):

        # populate missing_dict
        missing_dict = {}
        for idx in range(len(b)):
            if b[idx] == '.':
                row = int(idx / 9)
                col = idx % 9
                box = int(row / 3) * 3 + int(col / 3)
                values = set(get_row(row, b)).union(set(get_col(col, b))).union(set(get_box(box, b)))
                values.remove('.')
                missing_dict[idx] = numbers.difference(values)

        # check if complete
        if len(missing_dict) == 0:
            return create_board_from_list(b)

        # if a space has no possible value and the board is not complete we failed:
        if min(len(s) for s in missing_dict.values()) == 0:
            del b  # unsure of how garbage collection would work here
            return

        # store assured values
        n_missing_values = b.count('.')
        for idx, missings in missing_dict.items():
            if len(missings) == 1:
                v = missings.pop()
                b[idx] = v

        # check if no progress has been made
        if b.count('.') == n_missing_values:
            # min_key = min(missing_dict, key=lambda k: len(missing_dict[k]))
            # min_set = missing_dict[min_key]
            # if len(min_set) > 2:
            #     return
            for idx, s in missing_dict.items():
                if len(s) <= 3:
                    for v in s:
                        bb = b[:]
                        bb[idx] = v
                        go_through_recursive(bb)
            # else:
            #     for v in s:
            #         bb = b[:]
            #         bb[min_key] = v
            #         go_through_recursive(bb)


Solution().solveSudoku(board)
