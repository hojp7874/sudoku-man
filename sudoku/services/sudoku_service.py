import random


def generate_sudoku_problem():
    puzzle = [[0] * 9 for _ in range(9)]

    empty_cnt = 0
    while empty_cnt < 15:
        i, j, num = random.randint(0, 8), random.randint(0, 8), random.randint(1, 9)
        if is_valid(puzzle, num, i, j):
            puzzle[i][j] = num
            empty_cnt += 1

    return puzzle


def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None


def is_valid(board, num, i, j):
    # Check row
    if num in board[i]:
        return False

    # Check column
    if num in [board[i][j] for i in range(9)]:
        return False

    # Check 3x3 box
    box_i, box_j = i // 3 * 3, j // 3 * 3
    for row in board[box_i: box_i + 3]:
        if num in [e for e in row[box_j: box_j + 3]]:
            return False
    return True


def solve_sudoku(board):
    def backtracking():
        nonlocal board
        if (empty := find_empty_location(board)) is None:
            return True
        i, j = empty
        for num in range(1, 10):
            if is_valid(board, num, i, j):
                board[i][j] = num
                if backtracking():
                    return True
                board[i][j] = 0
        return False

    backtracking()

    return board
