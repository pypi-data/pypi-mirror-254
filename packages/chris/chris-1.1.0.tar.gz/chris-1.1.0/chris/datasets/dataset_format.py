"""Formats for datasets."""

from enum import StrEnum, auto


class DatasetFormat(StrEnum):
    """Formats for datasets."""

    JSON = auto()
    CSV = auto()
    TSV = auto()
