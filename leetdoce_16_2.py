from typing import List


class Sudoku:
    def solve_it(self, board: List[List[str]]) -> None:
        """
        :param board: sudoku board gets modified inplace at .create_board_from_list
        :return: None
        """
        unit_values = []
        for i in range(len(board)):  # flattening the board into unit_values
            for j in range(len(board[i])):
                unit_values.append(board[i][j])
        self.go_through_recursive(board, unit_values)

    def get_row(self, n: int, b):  # retrieve all elements of nth row in the board
        assert 0 <= n <= 8
        return set(b[9 * n: 9 * (n + 1)])

    def get_col(self, n: int, b):  # retrieve all elements of nth col in the board
        assert 0 <= n <= 8
        return set(b[n::9])

    def get_box(self, n: int, b):  # retrieve all elements of nth box in the board
        assert 0 <= n <= 8
        return set(b[i] for i in range(81) if (i // 27) == (n // 3) and i % 9 // 3 == n % 3)

    def go_through_recursive(self, board, b, d=False):
        """
        :param board: sudoku board as matrix where each row is a line
        :param b: sudoku board as a single long list
        """
        numbers = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
        while True:

            old_count = b.count('.')
            missing_dict = {}  # populate missing_dict
            for idx in range(len(b)):
                if b[idx] == '.':
                    row, col, box = idx // 9, idx % 9, (idx // 27) * 3 + (idx % 9) // 3
                    # union of all the present values in current row, col and box
                    values = self.get_row(row, b).union(self.get_col(col, b)).union(self.get_box(box, b))
                    values.remove('.')
                    missing_ones = numbers.difference(values)  # possible values to input in the slot
                    if len(missing_ones) == 0:  # impossible to continue
                        return False
                    elif len(missing_ones) == 1:
                        b[idx] = missing_ones.pop()
                    else:
                        missing_dict[idx] = missing_ones

            print(missing_dict)

            if b.count('.') == 0:  # check if complete
                self.create_board_from_list(board, b)
                return True

            if b.count('.') == old_count:  # if no progress has been made
                for idx, s in missing_dict.items():  # iterate through the dictionary
                    for number in s:  # create a new board and store indecisive value then recur
                        bb = b[:]
                        bb[idx] = number
                        if self.go_through_recursive(board, bb):
                            return True

    def create_board_from_list(self, board, b):
        temp_board = []
        chunk = 9
        for idx in range(0, len(b), chunk):
            temp_board.append(b[idx: idx + chunk])
        for idx in range(len(board)):
            board[idx] = temp_board[idx]
        print('done')


# board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
#          ["6", ".", ".", "1", "9", "5", ".", ".", "."],
#          [".", "9", "8", ".", ".", ".", ".", "6", "."],
#          ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
#          ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
#          ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#          [".", "6", ".", ".", ".", ".", "2", "8", "."],
#          [".", ".", ".", "4", "1", "9", ".", ".", "5"],
#          [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

board = [[".", ".", "9", "7", "4", "8", ".", ".", "."],
         ["7", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", "2", ".", "1", ".", "9", ".", ".", "."],
         [".", ".", "7", ".", ".", ".", "2", "4", "."],
         [".", "6", "4", ".", "1", ".", "5", "9", "."],
         [".", "9", "8", ".", ".", ".", "3", ".", "."],
         [".", ".", ".", "8", ".", "3", ".", "2", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "6"],
         [".", ".", ".", "2", "7", "5", "9", ".", "."]]

# board = [[".", ".", ".", "2", ".", ".", ".", "6", "3"],
#          ["3", ".", ".", ".", ".", "5", "4", ".", "1"],
#          [".", ".", "1", ".", ".", "3", "9", "8", "."],
#          [".", ".", ".", ".", ".", ".", ".", "9", "."],
#          [".", ".", ".", "5", "3", "8", ".", ".", "."],
#          [".", "3", ".", ".", ".", ".", ".", ".", "."],
#          [".", "2", "6", "3", ".", ".", "5", ".", "."],
#          ["5", ".", "3", "7", ".", ".", ".", ".", "8"],
#          ["4", "7", ".", ".", ".", "1", ".", ".", "."]]

# board = [[".", ".", ".", ".", ".", ".", ".", "6", "3"],
#          ["3", ".", ".", ".", ".", ".", "4", ".", "1"],
#          [".", ".", "1", ".", ".", "3", "9", "8", "."],
#          [".", ".", ".", ".", ".", ".", ".", "9", "."],
#          [".", ".", ".", ".", ".", "8", ".", ".", "."],
#          [".", "3", ".", ".", ".", ".", ".", ".", "."],
#          [".", ".", ".", "3", ".", ".", "5", ".", "."],
#          ["5", ".", "3", "7", ".", ".", ".", ".", "8"],
#          ["4", "7", ".", ".", ".", "1", ".", ".", "."]]


Sudoku().solve_it(board)


boards = [
        [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]],

        [[".", ".", "9", "7", "4", "8", ".", ".", "."],
         ["7", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", "2", ".", "1", ".", "9", ".", ".", "."],
         [".", ".", "7", ".", ".", ".", "2", "4", "."],
         [".", "6", "4", ".", "1", ".", "5", "9", "."],
         [".", "9", "8", ".", ".", ".", "3", ".", "."],
         [".", ".", ".", "8", ".", "3", ".", "2", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "6"],
         [".", ".", ".", "2", "7", "5", "9", ".", "."]],

        [[".", ".", ".", "2", ".", ".", ".", "6", "3"],
         ["3", ".", ".", ".", ".", "5", "4", ".", "1"],
         [".", ".", "1", ".", ".", "3", "9", "8", "."],
         [".", ".", ".", ".", ".", ".", ".", "9", "."],
         [".", ".", ".", "5", "3", "8", ".", ".", "."],
         [".", "3", ".", ".", ".", ".", ".", ".", "."],
         [".", "2", "6", "3", ".", ".", "5", ".", "."],
         ["5", ".", "3", "7", ".", ".", ".", ".", "8"],
         ["4", "7", ".", ".", ".", "1", ".", ".", "."]],

        [[".", ".", ".", ".", ".", ".", ".", "6", "3"],
         ["3", ".", ".", ".", ".", ".", "4", ".", "1"],
         [".", ".", "1", ".", ".", "3", "9", "8", "."],
         [".", ".", ".", ".", ".", ".", ".", "9", "."],
         [".", ".", ".", ".", ".", "8", ".", ".", "."],
         [".", "3", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", "3", ".", ".", "5", ".", "."],
         ["5", ".", "3", "7", ".", ".", ".", ".", "8"],
         ["4", "7", ".", ".", ".", "1", ".", ".", "."]]
]


# for i in range(100):
#     boa = boards[i % 4]
#     Sudoku().solve_it(boa)

print('end')


# def solve(board):
#     for i in range(9):
#         for j in range(9):
#             if board[i][j] == '.':
#                 for num in '123456789':
#                     if valid(board, i, j, num):
#                         board[i][j] = num
#                         if solve(board):
#                             return True
#                         else:
#                             board[i][j] = '.'  # undo the current cell for backtracking
#                 return False  # trigger backtracking
#     return True
#
#
# def valid(board, row, col, num):
#     # Check the number in the row, column and box.
#     for i in range(9):
#         if board[i][col] == num:
#             return False
#         if board[row][i] == num:
#             return False
#         if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num:
#             return False
#     return True
