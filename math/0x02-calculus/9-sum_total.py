#!/usr/bin/env python3
"""return the summation_i_squared"""


def summation_i_squared(n):
    """Function return summation_i_squared"""
    if n is None or n <= 0:
        return None
    return n * (n + 1) * (2 * n + 1) / 6
