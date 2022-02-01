#!/usr/bin/env python3
"""This script defines a function called sum_list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Computes the sum of a list of float numbers

    :param input_list(list(float)): List of float numbers

    return: float. Sum of the float numbers
    """
    return float(sum(input_list))
