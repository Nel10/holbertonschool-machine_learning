#!/usr/bin/env python3
"""Create Class DeepNeuralNetwork"""
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
            raise TypeError("layers must be a list of positive integers")
        negative = list(filter(lambda X: X <= 0, layers))
        if len(negative) > 0:
            raise TypeError("layers must be a list of positive integers")
        self.__L = len(layers)
        self.__cache = {}
        self.__weights = {}
        for i in range(len(layers)):
            if i == 0:
                factor1 = np.random.randn(layers[i], nx)
                self.weights['W{}'.format(i + 1)] = factor1 * np.sqrt(2/nx)
            else:
                factor1 = np.random.randn(layers[i], layers[i - 1])
                factor2 = np.sqrt(2/layers[i - 1])
                self.weights['W{}'.format(i + 1)] = factor1 * factor2
            self.weights['b{}'.format(i + 1)] = np.zeros((layers[i], 1))

    @property
    def L(self):
        """Return the L"""
        return self.__L

    @property
    def cache(self):
        """Return the cache"""
        return self.__cache

    @property
    def weights(self):
        """Return the weights"""
        return self.__weights

    def forward_prop(self, X):
        """Calculates the forward propagation of the neural network"""
        self.__cache['A0'] = X
        for i in range(self.__L):
            bias = self.__weights['b{}'.format(i+1)]
            z = np.dot(self.__weights['W{}'.format(i+1)], X) + bias
            predictions = sigmoid(z)
            X = predictions
            self.__cache['A{}'.format(i+1)] = predictions
        return predictions, self.__cache

    def cost(self, Y, A):
        """Calculates the cost of the model using logistic regression"""
        m = Y.shape[1]
        costs = Y * np.log(A) + (1 - Y) * np.log(1.0000001 - A)
        total_cost = -costs.sum() / m
        return total_cost

    def evaluate(self, X, Y):
        """Evaluates the neural network’s predictions"""
        prediction, caches = self.forward_prop(X)
        costs = self.cost(Y, prediction)
        prediction = np.rint(prediction).astype(int)
        return prediction, costs


def sigmoid(z):
    """Return the function Activate"""
    return 1 / (1 + np.exp(-z))
