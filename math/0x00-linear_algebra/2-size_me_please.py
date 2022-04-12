#!/usr/bin/env python3
"""Shadow for size the len of matrix"""


def matrix_shape(matrix):
    """Function for return shape"""
    shape = []
    while(type(matrix) is list):
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape
