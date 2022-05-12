#!/usr/bin/env python3
"""class Neuron that defines a single neuron"""
import numpy as np
import matplotlib.pyplot as plt


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
        """ the neuron’s prediction and the cost of the network"""
        prediction = self.forward_prop(X)
        total_cost = self.cost(Y, prediction)
        #  np.rint: Round elements of the array to the nearest integer.
        prediction = np.rint(prediction).astype(int)
        return prediction, total_cost

    def gradient_descent(self, X, Y, A, alpha=0.05):
        """calculate the gradient_descent for
        one neuron with proof chain rule"""
        m = Y.shape[1]  # calculate shape Y
        der_weight = np.dot((A - Y), np.transpose(X)) / m
        self.__W = self.__W - alpha * der_weight
        der_bias = np.sum(A - Y) / m
        self.__b = self.__b - alpha * der_bias

    def train(self, X, Y, iterations=5000, alpha=0.05, verbose=True,
              graph=True, step=100):
        """Calculate the evaluation of the training
        data after iterations of training have occurred"""
        if type(iterations) is not int:
            raise TypeError("iterations must be an integer")
        if iterations < 0:
            raise ValueError("iterations must be a positive integer")
        if type(alpha) is not float:
            raise TypeError("alpha must be a float")
        if alpha < 0:
            raise ValueError("alpha must be positive")

        if verbose is True and graph is True:
            if type(step) is not int:
                raise TypeError("step must be an integer")
            if step < 0 or step > iterations:
                raise ValueError("step must be positive and <= iterations")
        costs = []
        iters = []
        for i in range(iterations + 1):  # _ = no used variable
            prediction = self.forward_prop(X)
            self.__A = prediction
            self.gradient_descent(X, Y, self.__A, alpha)

            if verbose is True and (i % step) == 0:
                cost = self.cost(Y, self.__A)
                costs.append(cost)
                iters.append(i)
                print("Cost after {} iterations: {}".format(i, cost))

        if graph is True:
            plt.xlabel("iteration")
            plt.ylabel("cost")
            plt.title("Training Cost")
            plt.plot(iters, costs)

        return self.evaluate(X, Y)


def my_sigmoide(z):
    """calculate a function sigmoid"""
    return 1 / (1 + np.exp(-z))
