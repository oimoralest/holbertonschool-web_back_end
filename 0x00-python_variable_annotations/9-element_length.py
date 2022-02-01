#!/usr/bin/env python3
"""This script defines a function called element_length"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Unkown behavior"""
    return [(i, len(i)) for i in lst]
