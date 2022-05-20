#!/usr/bin/env python3
"""normalizes (standardizes)"""


def normalize(X, m, s):
    """
    X numpy.ndarray - matrix to normalize
    d is the number of data points
    nx is the number of features
    m is that contains the mean of all features of X
    s is the contains the standard deviation of all features of X
    """
    return (X - m) / s
