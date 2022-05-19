#!usr/bin/env python3
""""""
import numpy as np


class DeepNeuralNetwork():
    """defines a deep neural network
    performing binary classification"""

    def __init__(self, nx, layers):
        """
        L: The number of layers in the neural network.
        cache: A dictionary to hold all intermediary values of the network.
        weights: A dictionary to hold all weights and biased of the network

        """
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if type(layers) is not list or len(layers) == 0:
            raise TypeError("ayers must be a list of positive integers")
        negative = list(filter(lambda X: X <= 0, layers))
        if len(negative) > 0:
            raise TypeError("layers must be a list of positive integers")
        self.L = len(layers)
        self.cache = {}
        self.weights = {}
        for i in range(len(layers)):
            if i == 0:
                factor1 = np.random.randn(layers[i], nx)
                self.weights['W{}'.format(i + 1)] = factor1 * np.sqrt(2/nx)
            else:
                factor1 = np.random.randn(layers[i], layers[i - 1])
                factor2 = np.sqrt(2/layers[i - 1])
                self.weights['W{}'.format(i + 1)] = factor1 * factor2
            self.weights['b{}'.format(i + 1)] = np.zeros((layers[i], 1))
