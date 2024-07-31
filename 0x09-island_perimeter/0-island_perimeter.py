#!/usr/bin/python3
"""
Module 0-island_perimeter
"""


def island_perimeter(grid):
    """
    Iterative Approach: Iterates over each cell in the grid.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Start with a full perimeter for the cell
                perimeter += 4

                # Check the adjacent cells and subtract perimeter for shared
                # sides
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # One side shared with the cell above
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # One side shared with the cell to the left

    return perimeter
