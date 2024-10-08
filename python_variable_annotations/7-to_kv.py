#!/usr/bin/env python3
"""
This module provides a function that takes a string and an int or float,
and returns a tuple with the string and the square of the int/float.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple where the first element is the string `k`,
    and the second element is the square of `v`."""
    return (k, float(v ** 2))
