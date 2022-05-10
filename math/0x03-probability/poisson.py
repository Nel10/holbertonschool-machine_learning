#!/usr/bin/env python3
"""Create a class Poisson"""
e = 2.7182818285


class Poisson():
    """class Poisson that represents a poisson distribution"""

    def __init__(self, data=None, lambtha=1.):
        """
        data is a list of the data.
        lambtha is the expected, float
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(sum(data)/len(data))

    def pmf(self, k):
        """Function for calculate value PMF"""
        try:
            k = int(k)
        except Exception:
            return 0
        if k < 0:
            return 0
        PMF = (e ** (-self.lambtha) * self.lambtha ** (k)) / factorial(k)
        return PMF


def factorial(n):
    """Function for find factorial"""
    # 5! = 1 * 2 * 3 * 4 * 5
    # n! = 1 * 2 * 3 .. n
    num = 1
    for i in range(1, n + 1):
        num *= i
    return num
