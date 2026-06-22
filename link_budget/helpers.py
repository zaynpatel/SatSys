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
