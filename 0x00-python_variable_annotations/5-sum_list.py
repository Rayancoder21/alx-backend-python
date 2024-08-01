#!/usr/bin/env python3
"""
Complex types - list of floats
 function that takes a list input_list of floats as argument and returns their sum as a float.
"""
from typing import List

def sum_list(input_list: list[float]) -> float:
    """
    Typed-annotated function
    """
    return sum(input_list)
