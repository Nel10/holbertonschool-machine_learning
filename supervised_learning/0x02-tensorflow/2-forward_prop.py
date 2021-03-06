#!/usr/bin/env python3
"""creates the forward propagation graph """
import tensorflow.compat.v1 as tf
create_layer = __import__('1-create_layer').create_layer


def forward_prop(x, layer_sizes=[], activations=[]):
    """
    x is the placeholder for the input data
    layer_sizes is a list containing the number of nodes in each layer
    activations is a list containing the activation functions for each layer
    """
    prediction = x
    for i in range(len(layer_sizes)):
        prediction = create_layer(prediction, layer_sizes[i],
                                  activations[i])
    return prediction
