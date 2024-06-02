#!/usr/bin/python3
"""
0-pascal_triangle.py
"""


# n is num_rows
def pascal_triangle(n):
    """
    Generate Pascal's triangle up to n rows.
    """
    triangle = []

    if n <= 0:
        return triangle

    for row_num in range(n):
        # Start with a row of "1"s
        row = [1] * (row_num + 1)

        # Compute the values inside the row
        for j in range(1, row_num):
            row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]

        # Add the row to the triangle
        triangle.append(row)

    return triangle
