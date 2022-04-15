#!/usr/bin/env python3
"""Function that performs operations"""


def np_elementwise(mat1, mat2):
    """Return operations"""
    sum = mat1 + mat2
    sub = mat1 - mat2
    mul = mat1 * mat2
    div = mat1 / mat2
    return (sum, sub, mul, div)
