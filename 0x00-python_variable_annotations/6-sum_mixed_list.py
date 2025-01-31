#!/usr/bin/env python3
"""
Complex types - mixed list
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    typed-annotated function
    """
    return sum(mxd_lst)
