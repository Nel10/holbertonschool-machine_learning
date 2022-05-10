#!/usr/bin/env python3
"""Create a class Exponential"""
e = 2.7182818285


class Exponential():
    """Represents an exponential distribution"""

    def __init__(self, data=None, lambtha=1.):
        """
        data is a list of the data
        lambtha is the expected number
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
            mean = sum(data) / len(data)
            self.lambtha = 1 / float(mean)

    def pdf(self, x):
        """Calculate a value PDF"""
        if x < 0:
            return 0
        PDF = self.lambtha * e ** (-self.lambtha * x)
        return PDF

    def cdf(self, x):
        """Calculate a value CDF"""
        if x < 0:
            return 0
        CDF = 1 - e ** (-self.lambtha * x)
        return CDF
