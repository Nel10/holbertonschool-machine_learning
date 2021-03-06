#!/usr/bin/env python3
"""Initialize Binomial"""


class Binomial():
    """Create a class Binomial"""

    def __init__(self, data=None, n=1, p=0.5):
        """
        data is a list.
        n is the number of Bernoulli trials
        p is the probability of a “success”
        """
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if p <= 0 or p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = int(n)
            self.p = float(p)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            mean = sum(data) / len(data)
            # mean = n * p
            sumat = 0
            for x in data:
                sumat += (x - mean) ** 2
            stddev = ((1 / len(data)) * sumat) ** 0.5
            varianza = stddev ** 2
            # varianza = n * p * (1 - p)
            # mean / varianza = n * p / n * p * (1 - p)
            # mean / varianza = 1 / (1 - p)
            p = 1 - (varianza / mean)
            self.n = round(mean / p)
            self.p = mean / self.n

    def pmf(self, k):
        """Return the value PMF"""
        try:
            if type(k) is not int:
                k = int(k)
        except Exception:
            return 0
        if k < 0:
            return 0
        com = factorial(self.n) / (factorial(k) * factorial(self.n - k))
        PMF = com * (self.p ** k) * ((1 - self.p) ** (self.n - k))
        return PMF

    def cdf(self, k):
        """calculate the value CDF"""
        try:
            if type(k) is not int:
                k = int(k)
        except Exception:
            return 0
        sumat = 0
        for i in range(k + 1):
            sumat += self.pmf(i)
        return sumat


def factorial(n):
    """Return factorial number"""
    # n! = 1 * 2 * 3 .. n
    num = 1
    for i in range(1, n + 1):
        num *= i
    return num
