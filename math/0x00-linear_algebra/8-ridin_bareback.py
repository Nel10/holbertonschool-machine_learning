#!/usr/bin/env python3
"""Function for mult matrices"""


def mat_mul(mat1, mat2):
    """Return the new_matrix"""
    new_matrix = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat2[0])):
            sum = 0
            for k in range(len(mat2)):
                sum += mat1[i][k] * mat2[k][j]
            row.append(sum)
        new_matrix.append(row)
    return new_matrix
