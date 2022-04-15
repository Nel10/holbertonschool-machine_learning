#!/usr/bin/env python3
"""Function for concatenate matrices2D"""


def is_list(matrix):
    """ returns True if the matrix is a list """
    return type(matrix) is list


def matrix_shape(matrix):
    """ Returns the shape of the matrix"""
    if type(matrix) != list or not matrix:
        return [0, ]
    return [len(matrix), *matrix_shape(matrix[0])]


def equal_without(matrix1, matrix2, without=0, index=0):
    """Returns true if the two matrices are equal without any index"""

    if without != -1:
        del matrix1[without]
        del matrix2[without]
        without = -1

    if index >= len(matrix1):
        return True

    try:
        if matrix1[index] != matrix2[index]:
            return False
    except IndexError:
        return True

    return equal_without(matrix1, matrix2, without, index + 1)


def cat_matrices2D(mat1, mat2, axis=0, firts=True):
    """ Concat matrices to a single matrix """
    if not is_list(mat1) and not is_list(mat2):
        return None

    shape_one = matrix_shape(mat1)
    shape_two = matrix_shape(mat2)
    if firts and not equal_without(shape_one, shape_two, axis):
        return None

    if (axis == 0):
        return [*mat1, *mat2]

    result = list(range(len(mat1)))
    for i in range(len(mat1)):
        result[i] = cat_matrices2D(mat1[i], mat2[i], axis - 1, False)
    return result
