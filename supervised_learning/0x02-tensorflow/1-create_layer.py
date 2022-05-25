#!/usr/bin/env python3
"""initialization for the layer weights"""
import tensorflow.compat.v1 as tf


def create_layer(prev, n, activation):
    """
    prev is the tensor output of the previous layer
    n is the number of nodes in the layer to create
    activation is the activation function that the layer should use
    """
    weights = tf.keras.initializers.VarianceScaling(mode='fan_avg')
    layers = tf.keras.layers.Dense(units=n, activation=activation,
                                   kernel_initializer=weights, name='layer')
    return layers(inputs=prev)
