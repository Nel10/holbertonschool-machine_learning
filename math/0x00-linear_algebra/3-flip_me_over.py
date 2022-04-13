#!/usr/bin/env python3
"""Funtion for list matrix"""


def matrix_transpose(matrix):
    """Return list_matrix"""
    list_matrix = []
    new_matrix = zip(*matrix)
    for item in new_matrix:
        list_matrix.append(list(item))

    return list_matrix
