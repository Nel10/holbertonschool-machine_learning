#!/usr/bin/env python3
"""creates a confusion matrix"""
import numpy as np


def create_confusion_matrix(labels, logits):
    """
    m is the number of data points
    classes is the number of classes
    """
    K = len(labels[0])
    # Initialize the confusion matrix
    result = np.zeros((K, K))
    # numpy.where(condition, [x, y, ]/)
    # Return elements chosen from x or y depending on condition.
    labelsn = np.where(labels == 1)[1]
    logitsn = np.where(logits == 1)[1]
    for i in range(len(labelsn)):
        result[labelsn[i]][logitsn[i]] += 1
    return result
