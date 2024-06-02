#!/usr/bin/python3
"""
0-pascal_triangle.py
"""


def pascal_triangle(num_rows):
    """
    Generate Pascal's triangle up to n rows.
    """
    triangle = []

    if num_rows <= 0:
        return triangle

    for row_num in range(num_rows):
        # Start with a row of "1"s
        row = [1] * (row_num + 1)

        # Compute the values inside the row
        for j in range(1, row_num):
            row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]

        # Add the row to the triangle
        triangle.append(row)

    return triangle
