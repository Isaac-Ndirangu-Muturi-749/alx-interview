#!/usr/bin/env python3
"""module 0-nqueens"""

import sys


def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]."""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(n):
    """Solve the N Queens problem and print all solutions."""
    def place_queens(row):
        if row == n:
            solution = []
            for i in range(n):
                solution.append([i, board[i]])
            solutions.append(solution)
        else:
            for col in range(n):
                if is_safe(board, row, col):
                    board[row] = col
                    place_queens(row + 1)

    board = [-1] * n
    solutions = []
    place_queens(0)
    return solutions


def main():
    """Main function to handle input and output."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(n)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
