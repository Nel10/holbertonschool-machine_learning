#!/usr/bin/env python3
"""Function return a derivate"""


def poly_derivative(poly):
    """return derivate"""
    if type(poly) is not list:
        return None
    derivate = []
    for i in range(len(poly)):
        if i >= 1:
            derivate.append(poly[i] * i)
    return derivate
