#!/usr/bin/env python3
"""calculates the softmax cross-entropy loss of a prediction"""
import tensorflow.compat.v1 as tf


def calculate_loss(y, y_pred):
    """
    y is a placeholder for the labels of the input data
    y_pred is a tensor containing the network’s predictions
    """
    return tf.nn.softmax_cross_entropy_with_logits(y, y_pred)
