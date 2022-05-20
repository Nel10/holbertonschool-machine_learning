#!/usr/bin/env python3
"""calculates the normalization
(standardization) constants of a matrix
"""
import numpy as np


def normalization_constants(X):
    """
    m is the number of data points
    nx is the number of features
    Returns: the mean and standard deviation of each feature
    """
    return np.mean(X, axios=0), np.std(X, axios=0)
