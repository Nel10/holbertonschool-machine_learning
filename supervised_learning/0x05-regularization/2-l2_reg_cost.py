#!/usr/bin/env python3
"""L2 Regularization cost"""
import tensorflow.compat.v1 as tf


def l2_reg_cost(cost):
    """
    cost is a tensor containing the cost of the network without L2
    regularization
    Returns: a tensor containing the cost of the network accounting for L2
    regularization
    """
    return cost + tf.losses.get_regularization_losses()
