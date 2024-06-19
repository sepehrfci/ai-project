import numpy as np
import random


class Sudoku:
    def __init__(self, board):
        self.board = np.array(board, dtype=int)

    def is_valid(self, row, col, num):
        #Check if a number can be placed at a specific position.
        for i in range(9):
            if self.board[row][i] == num or self.board[i][col] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.board[start_row + i][start_col + j] == num:
                    return False
        return True

    def find_empty_location(self):
        #Find an empty location on the board.
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return i, j
        return None

    def solve(self):
        #Solve the Sudoku puzzle using backtracking.
        empty_loc = self.find_empty_location()
        if not empty_loc:
            return True
        row, col = empty_loc

        for num in range(1, 10):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.solve():
                    return True
                self.board[row][col] = 0
        return False

    def display(self):
        #Display the Sudoku board.
        for row in self.board:
            print(" ".join(map(str, row)))



initial_board = np.array([
    [0, 2, 0, 0, 0, 0, 0, 0, 7],
    [1, 0, 8, 4, 9, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 3, 0],
    [0, 0, 0, 0, 0, 2, 0, 5, 0],
    [0, 8, 7, 0, 0, 0, 6, 0, 9],
    [0, 6, 0, 5, 0, 0, 0, 0, 0],
    [9, 0, 0, 0, 0, 8, 0, 0, 0],
    [0, 0, 0, 0, 3, 9, 5, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 2]
])

sudoku_solver = Sudoku(initial_board)
print("Initial Sudoku board:")
sudoku_solver.display()

if sudoku_solver.solve():
    print("\nSudoku solved successfully:")
    sudoku_solver.display()
else:
    print("No solution exists.")
