#!/usr/bin/env python3
"""This script defines a function called sum_mixed_list"""
from typing import List, Union

Num = Union[int, float]


def sum_mixed_list(mxd_lst: List[Num]) -> float:
    """Computes the sum of a mixed list of float and integer numbers"""
    return float(sum(mxd_lst))
