#!/usr/bin/env python3
"""Function sum the matrix"""


def add_matrices2D(mat1, mat2):
    """Return sum_matrix"""
    if len(mat1[0]) != len(mat2[0]):
        return None
    sum_matrix = []
    for row in range(len(mat1)):
        lit = []
        for i in range(len(mat1[0])):
            lit.append(mat1[row][i] + mat2[row][i])
        sum_matrix.append(lit)
    return sum_matrix
