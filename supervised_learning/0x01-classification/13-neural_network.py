#!/usr/bin/env python3
"""Create a class NeuralNetwork"""
import numpy as np


class NeuralNetwork():
    """
    class NeuralNetwork that defines a neural network
    with one hidden layer performing binary classification
    """

    def __init__(self, nx, nodes):
        """
        nx is the number of input features.
        nodes is the number of nodes found in the hidden layer.
        W1: The weights vector for the hidden layer.
        b1: The bias for the hidden layer.
        A1: The activated output for the hidden layer.
        W2: The weights vector for the output neuron.
        b2: The bias for the output neuron.
        A2: The activated output for the output neuron (prediction)
        """
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if type(nodes) is not int:
            raise TypeError("nodes must be an integer")
        if nodes < 1:
            raise ValueError("nodes must be a positive integer")
        self.__W1 = np.random.normal(size=(nodes, nx))
        self.__b1 = np.zeros((nodes, 1))
        self.__A1 = 0
        self.__W2 = np.random.normal(size=(1, nodes))
        self.__b2 = 0
        self.__A2 = 0

    @property
    def W1(self):
        """Return the value W1"""
        return self.__W1

    @property
    def b1(self):
        """Return the value b1"""
        return self.__b1

    @property
    def A1(self):
        """Return the value A1"""
        return self.__A1

    @property
    def W2(self):
        """Return the value W2"""
        return self.__W2

    @property
    def b2(self):
        """Return the value b2"""
        return self.__b2

    @property
    def A2(self):
        """Return the value A2"""
        return self.__A2

    def forward_prop(self, X):
        """Calculates the forward propagation of the neural network"""
        """first calculate the ponderation"""
        z = np.dot(self.__W1, X) + self.__b1
        """calculate the prediction for hidden layer"""
        self.__A1 = sigmoid(z)
        """output hidden layer = input for the output neuron"""
        z2 = np.dot(self.__W2, self.__A1) + self.__b2
        self.__A2 = sigmoid(z2)
        return self.__A1, self.__A2

    def cost(self, Y, A):
        """Calculates the cost of the model using logistic regression"""
        m = Y.shape[1]
        cost = -(Y * np.log(A) + (1 - Y) * np.log(1.0000001 - A)).sum()
        return cost / m

    def evaluate(self, X, Y):
        """Evaluates the neural network’s predictions"""
        prediction1, prediction2 = self.forward_prop(X)
        total_cost = self.cost(Y, prediction2)
        prediction2 = np.rint(prediction2).astype(int)
        return prediction2, total_cost

    def gradient_descent(self, X, Y, A1, A2, alpha=0.05):
        """Calculates one pass of gradient
        descent on the neural network"""
        """m is the number of examples"""
        m = Y.shape[1]
        der_cos_z_L = A2 - Y
        """ der_cos_w = der_cos_z * der_z_w"""
        der_cos_w_L = np.dot(A1, der_cos_z_L.T) / m
        """ update weigths """
        self.__W2 = self.__W2 - (alpha * der_cos_w_L.T)
        """Axis = 0 sum by columns, axis = 1, sum by rows"""
        der_cos_b_L = np.sum(der_cos_z_L, axis=1, keepdims=True) / m
        self.__b2 = self.__b2 - alpha * der_cos_b_L
        error_L_1 = np.dot(self.__W2.T, der_cos_z_L) * deriv_sigmoid(A1)
        der_cos_w_L_1 = np.dot(X, error_L_1.T) / m
        self.__W1 = self.__W1 - (alpha * der_cos_w_L_1.T)
        der_cos_b_L_1 = np.sum(error_L_1,  axis=1, keepdims=True) / m
        self.__b1 = self.__b1 - alpha * der_cos_b_L_1


def deriv_sigmoid(A):
    """function return deriv_sigmoid"""
    return A * (1 - A)


def sigmoid(z):
    """return sigmoid function"""
    return 1 / (1 + np.exp(-z))
