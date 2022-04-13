#!/usr/bin/env python3
"""Function for concatenate matrices2D"""


def mydeepcopy(L):
    """Function for deep copy"""
    if isinstance(L, list):
        ret = []
        for i in L:
            ret.append(mydeepcopy(i))
    elif isinstance(L, (int, float, type(None), str, bool)):
        ret = L
    else:
        raise ValueError("Unexpected type for mydeepcopy function")

    return ret


def cat_matrices2D(mat1, mat2, axis=0):
    """concatenate matrices2D"""
    new_matrix = []
    mat1_cpy = mydeepcopy(mat1)
    mat2_cpy = mydeepcopy(mat2)

    if axis == 0:
        new_matrix = mat1_cpy + mat2_cpy
        return new_matrix
    for i in range(len(mat2_cpy)):
        mat1_cpy[i] = mat1_cpy[i] + mat2_cpy[i]
    return mat1_cpy
