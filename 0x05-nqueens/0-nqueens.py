#!/usr/bin/python3
"""N-Queens Solver"""

import sys


def is_safe(board, row, col, size):
    """
    Check if placing a queen at board[row][col] is safe.
    """
    # Check if there is a queen in the same column
    for r in range(row):
        if board[r][col] == 1:
            return False

    # Check upper-left diagonal
    r, c = row, col
    while r >= 0 and c >= 0:
        if board[r][c] == 1:
            return False
        r -= 1
        c -= 1

    # Check upper-right diagonal
    r, c = row, col
    while r >= 0 and c < size:
        if board[r][c] == 1:
            return False
        r -= 1
        c += 1

    # If no conflicts, it's safe to place a queen at board[row][col]
    return True


def solve(board, row, size):
    """
    Recursively find all solutions to the N-Queens problem.
    """
    if row == size:
        # Base case: If all rows are covered, print the solution
        print([[r, c] for r in range(size)
               for c in range(size) if board[r][c] == 1])
        return True

    for col in range(size):
        if is_safe(board, row, col, size):
            # If it's safe to place a queen, mark board[row][col] as 1
            board[row][col] = 1

            # Recursively call solve for the next row
            solve(board, row + 1, size)

            # Backtrack: Reset board[row][col] to 0 for other solutions
            board[row][col] = 0

    return False


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        size = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if size < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize an n x n board with zeros
    board = [[0 for col in range(size)] for row in range(size)]

    # Call solve function to find and print all solutions
    solve(board, 0, size)
