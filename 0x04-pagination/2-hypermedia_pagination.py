#!/usr/bin/env python3
import csv
from typing import List
from typing import Tuple
import math


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
        """Return data for a given page and page size"""
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        start_index, end_index = index_range(page=page, page_size=page_size)

        dataset = (
            self.__dataset if self.__dataset is not None else self.dataset()
        )
        if start_index > len(dataset):
            return []

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Retun a json like content of a page"""
        data = self.get_page(page=page, page_size=page_size)

        return {
            "page_size": page_size if data else 0,
            "page": page if data or len(self.__dataset) > page else 0,
            "data": data,
            "next_page": (
                page + 1
                if page + 1 < math.ceil(len(self.__dataset) / page_size)
                else None
            ),
            "prev_page": page - 1 if page - 1 > 0 else None,
            "total_pages": math.ceil(len(self.__dataset) / page_size)
        }
