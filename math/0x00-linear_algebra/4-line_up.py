#!/usr/bin/env python3
"""Function for sum list"""


def add_arrays(arr1, arr2):
    """return sum_list"""
    if len(arr1) != len(arr2):
        return None
    sum_list = []
    for i in range(len(arr1)):
        sum_list.append(arr1[i] + arr2[i])
    return sum_list
