import numpy as np
import random


# تولید یک جدول سودوکوی معتبر
def generate_valid_board():
    board = np.zeros((9, 9), dtype=int)
    for i in range(9):
        num_list = list(range(1, 10))
        for j in range(9):
            if random.random() < 0.3:  # 30% از خانه‌ها را پر می‌کنیم
                while num_list:
                    num = random.choice(num_list)
                    if is_valid(board, i, j, num):
                        board[i, j] = num
                        break
                    num_list.remove(num)
    return board

# بررسی معتبر بودن عدد در موقعیت خاص
def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True


def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def solve_sudoku(board):
    empty_loc = find_empty_location(board)
    if not empty_loc:
        return True
    row, col = empty_loc
    
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    return False

# مثال یک پازل سودوکو (0 نشان‌دهنده خانه‌های خالی است)
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# sudoku_board = generate_valid_board()

for row in sudoku_board:
    print(row)

if solve_sudoku(sudoku_board):
    print("سودوکو با موفقیت حل شد:")
    for row in sudoku_board:
        print(row)
else:
    print("راه‌حلی وجود ندارد")