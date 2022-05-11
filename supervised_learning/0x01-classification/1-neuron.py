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
