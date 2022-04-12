#!/usr/bin/env python3
""""""


def add_matrices2D(mat1, mat2):
    """"""
    if len(mat1) != len(mat2):
        return None
    sum_matrix = []
    for i in range(len(mat1)):
        sum_matrix.append(mat1[i], mat2[i])
    return sum_matrix
