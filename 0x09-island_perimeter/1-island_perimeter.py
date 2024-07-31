#!/usr/bin/python3
"""
Module 1-island_perimeter
"""


def island_perimeter(grid):
    """
    DFS Approach: Uses depth-first search to explore the island.
    """
    visited = set()

    def dfs(row, col):
        # If the cell is out of bounds or water, it contributes to the
        # perimeter
        if row < 0 or col < 0 or row >= len(
                grid) or col >= len(grid[0]) or grid[row][col] == 0:
            return 1
        # If the cell is already visited, it does not contribute to the
        # perimeter
        if (row, col) in visited:
            return 0
        # Mark the cell as visited
        visited.add((row, col))
        # Explore all four directions and sum up the perimeter contributions
        perimeter = dfs(row, col + 1)
        perimeter += dfs(row + 1, col)
        perimeter += dfs(row, col - 1)
        perimeter += dfs(row - 1, col)
        return perimeter

    # Find the first land cell and start the DFS from there
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                return dfs(row, col)
    return 0
