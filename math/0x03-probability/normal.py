#!/usr/bin/env python3
"""Create a class Normal"""


class Normal():
    """Represents a normal distribution"""

    def __init__(self, data=None, mean=0., stddev=1.):
        """
        data is a list of the data
        mean is the mean of the distribution
        stddev is the standard deviation
        """
        if data is None:
            self.stddev = float(stddev)
            self.mean = float(mean)
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.mean = float(sum(data) / len(data))
            sumat = 0
            for x in data:
                sumat += (x - self.mean) ** 2
            self.sttdev = float((1 / len(data) * sumat) ** 0.5)
