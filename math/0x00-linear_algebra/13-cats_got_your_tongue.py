#!/usr/bin/env python3
"""function that concatenate"""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """return concatenate"""
    return np.concatenate((mat1, mat2), axis=axis)
