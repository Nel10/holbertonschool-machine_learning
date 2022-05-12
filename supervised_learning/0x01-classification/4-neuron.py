#!/usr/bin/env python3
"""class Neuron that defines a single neuron"""
import numpy as np


class Neuron():
    """
    nx is the number of input features to the Neuron.
    W: The weights vector for the Neuron.
    b: The bias for the neuron.
    A: The activated output of the neuron (prediction).
    """

    def __init__(self, nx):
        """Initialize a class Neuron"""
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        # np.random.normal(loc=mean,scale=standard_deviation, size=samples)
        # Loc: This parameter defaults to 0
        # Scale: By default, the scale parameter is set to 1.
        self.__W = np.random.normal(size=(1, nx))
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        """Getter to Weight"""
        return self.__W

    @property
    def b(self):
        """Getter to bias"""
        return self.__b

    @property
    def A(self):
        """Getter to prediction"""
        return self.__A

    def forward_prop(self, X):
        """Calculates the forward propagation of the neuron"""
        z = np.dot(self.__W, X) + self.__b
        output = my_sigmoide(z)
        self.__A = output
        return self.__A

    def cost(self, Y, A):
        """Calculate the value of cost between prediction
        of data real(y) and prediction of data for each neuron(A)"""
        m = len(np.transpose(Y))  # len(Y.T)
        cross_entr = -(Y * np.log(A) + (1 - Y) * np.log(1.0000001 - A)).sum()
        return cross_entr / m

    def evaluate(self, X, Y):
        """"""
        prediction = self.forward_prop(X)
        total_cost = self.cost(Y, prediction)
        #  np.rint: Round elements of the array to the nearest integer.
        prediction = np.rint(prediction).astype(int)
        return prediction, total_cost


def my_sigmoide(z):
    """calculate a function sigmoid"""
    return 1 / (1 + np.exp(-z))
