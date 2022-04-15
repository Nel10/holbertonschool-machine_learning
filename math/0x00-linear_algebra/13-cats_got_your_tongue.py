#!/usr/bin/env python3
import numpy as np
"""function that concatenate"""


def np_cat(mat1, mat2, axis=0):
    """return concatenate"""
    return np.concatenate((mat1, mat2), axis=axis)
