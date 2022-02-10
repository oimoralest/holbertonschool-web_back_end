#!/usr/bin/env python3
"""
This script defines a function named index_range
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return the start and end indexes of a page

    :param page(int): page number
    :param page_size(int): page size

    return: Tuple(start_index, end_index)
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index
