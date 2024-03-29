#!/usr/bin/env python3
"""Calculate the determinant"""


def determinant(matrix):
    """function that calculates the determinant of a matrix"""

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list of lists")
    if not all([isinstance(element, list) for element in matrix]):
        raise TypeError("matrix must be a list of lists")
    if len(matrix) == 0:
        raise TypeError("matrix must be a list of lists")

    # Infer the number of rows/columns in matrix
    height = len(matrix)
    width = len(matrix[0])

    # Edge case [[]] (0x0 matrix)
    if height == 1 and width == 0:
        return 1

    if height != width:
        raise ValueError("matrix must be a square matrix")
    if not all([len(matrix[i]) == width for i in range(1, height)]):
        raise ValueError("matrix must be a square matrix")

    # Account for edge case [[num]] (1x1 matrix)
    if height == 1 and width == 1:
        return matrix[0][0]

    # Exit condition: 2x2 submatrix reached
    if height == 2 and width == 2:
        sub_det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        return sub_det

    det = 0
    # Iterate through the column indices
    for col_index in range(width):
        # Slice the submatrix (remove first row)
        submat = matrix[1:]
        new_height = len(submat)
        # Iterate through the row indices of submat
        # and remove the column value at col_index
        for row_index in range(new_height):
            submat[row_index] = (submat[row_index][0: col_index] +
                                 submat[row_index][col_index + 1:])
        # Handle +/- sign
        sign = (-1) ** (col_index % 2)
        # This (ternary) also works:
        # sign = (-1) if (col_index % 2) != 0 else 1
        # Recursive call
        sub_det = determinant(submat)
        det += sign * matrix[0][col_index] * sub_det

    return det
