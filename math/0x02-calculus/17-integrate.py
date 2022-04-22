#!/usr/bin/env python3
"""Poly Integrate"""


def poly_integral(poly, C=0, power=1):
    """return integrals"""
    if type(poly) is not list or type(C) not in (int, float):
        return None
    coefficient, *poly = [*poly, None]
    integrals = [C] if power == 1 else []
    if coefficient is None:
        return []
    if coefficient == 0:
        return [*integrals, 0, *poly_integral(poly, C, power + 1)]
    if power != 0:
        return [*integrals, coefficient / power,
                *poly_integral(poly, C, power + 1)]
    return [*integrals, coefficient, *poly_integral(poly, C, power + 1)]
