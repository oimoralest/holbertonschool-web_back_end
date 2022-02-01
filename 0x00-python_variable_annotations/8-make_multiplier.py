#!/usr/bin/env python3
"""This script defines a function called make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Takes a float and returns a function that multiplies the float by
    other float

    :param multiplier(float): Float number

    return: fun. Function that multiplies two float numbers
    """
    def _mul(n: float) -> float:
        """Multiplies two float numbers

        :param n(float): second float number

        return: float. Multiplication of two float numbers
        """
        return float(multiplier * n)

    return _mul
