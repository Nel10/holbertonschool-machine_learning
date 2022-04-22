#!/usr/bin/env python3
def summation_i_squared(n):
    if type(n) != int and n <= 0:
        return None
    return (n*(n + 1)*(2*n + 1))/6
