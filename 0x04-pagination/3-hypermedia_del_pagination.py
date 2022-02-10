#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
       """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Args:
            index: int i defaults to none
            page_size: page size int defaults to 10
        Returns:
            dictionary with the following key-value pairs:
                index: the current start index of the return page.
                next_index: the next index to query with.
                page_size: the current page size
                data: the actual page of the dataset
        """
        assert type(index) == int and type(page_size) == int
        assert len(self.indexed_dataset()) > index >= 0

        data = []
        next_index = index + page_size
        for item in range(index, index + page_size):
            if not self.indexed_dataset().get(item):
                item += 1
                next_index += 1
            data.append(self.indexed_dataset()[item])
        return {"data": data,
                "index": index,
                "next_index": next_index,
                "page_size": page_size
                }
