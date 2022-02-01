#!/usr/bin/env python3
"""This script defines a function called to_kv"""
from typing import Tuple, Union

Num = Union[int, float]


def to_kv(k: str, v: Num) -> Tuple[str, float]:
    """Returns a tuple compose by an string and a float number

    :param k(str): String
    :param v(float or int): Number

    return: Tuple. String and float number which is the square of v
    """
    return k, float(v ** 2)
