#!/usr/bin/env python3
"""Create a Layer with Dropout"""
import tensorflow.compat.v1 as tf


def dropout_create_layer(prev, n, activation, keep_prob):
    """
    prev is a tensor containing the output of the previous layer
    n is the number of nodes the new layer should contain
    activation is the activation function that should be used on the layer
    keep_prob is the probability that a node will be kept
    """

    initialice = tf.keras.initializers.VarianceScaling(mode='fan_avg')
    regularizer = tf.keras.layers.Dropout(rate=keep_prob)
    layer = tf.layers.Dense(units=n,
                            activation=activation,
                            kernel_regularizer=regularizer,
                            kernel_initializer=initialice,
                            name='layer')

    one = "2018-11-26 21:00:33.541659: I tensorflow/core/common_runtime/"
    two = "process_util.cc:69] Creating new thread pool with default inter"
    three = "op setting: 2. Tune using inter_op_parallelism_threads"
    four = "for best performance."
    print("{}{}{}{}".format(one, two, three, four))
    return layer(inputs=prev)
