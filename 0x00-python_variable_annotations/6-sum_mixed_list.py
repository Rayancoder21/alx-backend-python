#!/usr/bin/env python3
"""
task6: Complex types - mixed list
function that takes a list mxd_lst of integers and floats and returns their sum as a float.
"""
from typing import Union, List

def sum_mixed_list(mxd_lst: List[Union[int,float]]) -> float:
    """
    typed-annotated function 
    """
    return sum(mxd_lst)
