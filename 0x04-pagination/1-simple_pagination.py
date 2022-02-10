#!/usr/bin/env python3
"""This script defines a Server class that return fake content by pages"""
import csv
from typing import List
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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        start_index, end_index = index_range(page=page, page_size=page_size)

        dataset = (
            self.__dataset if self.__dataset is not None else self.dataset()
        )
        if start_index > len(dataset):
            return []

        return dataset[start_index:end_index]
