"""
Docstring for link_budget.helpers
"""

import math


def power_ratio(db_value, ndigits=2):
    """
    Docstring for power_ratio
    """
    power = 10 ** (db_value / 10)
    return round(power, ndigits)

def power_ratio_to_decibels(power_measured, power_reference, ndigits):
    """..."""
    return round(10 * (math.log(power_measured / power_reference, 10)), ndigits)

def convert_degrees_to_radians(degrees: float):
    return degrees * (math.pi / 180)

def convert_radians_to_degrees(radians: float):
    return radians * (180 / math.pi)
