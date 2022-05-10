#!/usr/bin/env python3
"""Create a class Normal"""
pi = 3.1415926536
e = 2.7182818285


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
            self.mean = sum(data) / len(data)
            sumat = 0
            for x in data:
                sumat += (x - self.mean) ** 2
            self.stddev = (1 / len(data) * sumat) ** 0.5

    def z_score(self, x):
        """Calculates the z-score of a given x-value"""
        z = (x - self.mean) / self.stddev
        return z

    def x_value(self, z):
        """Calculates the x-value of a given z-score"""
        x = self.stddev * z + self.mean
        return x

    def pdf(self, x):
        """Calculates the value PDF"""
        exp = e ** (- 1 / 2 * ((x - self.mean) / self.stddev) ** 2)
        PDF = (1 / (self.stddev * (2 * pi) ** 0.5)) * exp
        return PDF

    def cdf(self, x):
        """Calculates the value CDF"""
        CDF = 1 / 2 * 1 + self.erf((x - self.mean) / (self.stddev * (2**0.5)))
        return CDF

    def erf(self, x):
        """Return the error function (erf)"""
        sumat = x - (x**3) / 3 + (x**5) / 10 + (x**7) / 42 + (x**9) / 216
        return (2 / (pi ** (0.5))) * sumat
