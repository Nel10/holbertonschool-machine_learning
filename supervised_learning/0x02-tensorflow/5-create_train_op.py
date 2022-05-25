#!/usr/bin/env python3
"""creates the training operation for the network"""
import tensorflow.compat.v1 as tf


def create_train_op(loss, alpha):
    """
    loss is the loss of the network’s prediction
    alpha is the learning rate
    """
    optimization = tf.train.GradientDescentOptimizer(learning_rate=alpha)
    return optimization.minimize(loss=loss)
