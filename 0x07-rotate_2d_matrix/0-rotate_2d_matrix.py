#!/usr/bin/python3
"""0-rotate_2d_matrix.py"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise.
    The rotation is done in place.
    """
    n = len(matrix)  # Get the size of the matrix (n x n)

    # Loop through each layer (or ring) of the matrix from outermost to
    # innermost
    for layer in range(n // 2):
        first = layer  # Index of the first element in the layer
        last = n - 1 - layer  # Index of the last element in the layer

        # Loop through the elements in the current layer
        for i in range(first, last):
            # Offset is used to move elements within the layer
            offset = i - first
            # Save the top element temporarily
            top = matrix[first][i]

            # Move the left element to the top
            matrix[first][i] = matrix[last - offset][first]

            # Move the bottom element to the left
            matrix[last - offset][first] = matrix[last][last - offset]

            # Move the right element to the bottom
            matrix[last][last - offset] = matrix[i][last]

            # Move the saved top element to the right
            matrix[i][last] = top
