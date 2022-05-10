#!/usr/bin/env python3
"""Create a class Exponential"""


class Exponential():
    """Represents an exponential distribution"""

    def __init__(self, data=None, lambtha=1.):
        """
        data is a list of the data
        lambtha is the expected number
        """
        if data is None:
            if lambtha < 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(self.lambtha)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            mean = sum(data) / len(data)
            self.lambtha = float(1 / mean)
