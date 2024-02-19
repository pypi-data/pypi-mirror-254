"""
MISCELLANEOUS helper functions
"""

from typing import NamedTuple, List, Dict

from .readwrite import read_csv
from .constants import STATE_FIPS


class Assignment(NamedTuple):
    geoid: str
    district: int | str


def starting_seed(xx: str, N: int, K: int = 1) -> int:
    fips: str = STATE_FIPS[xx]
    start: int = K * N * int(fips)

    return start


### END ###
