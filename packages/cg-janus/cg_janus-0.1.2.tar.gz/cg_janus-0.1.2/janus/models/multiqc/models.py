"""Models for the MultiQC intermediate JSON files."""

from pydantic import BaseModel


class PicardInsertSize(BaseModel):
    MEDIAN_INSERT_SIZE: float
    MODE_INSERT_SIZE: float
    MEDIAN_ABSOLUTE_DEVIATION: float
    MIN_INSERT_SIZE: float
    MAX_INSERT_SIZE: float
    MEAN_INSERT_SIZE: float
    STANDARD_DEVIATION: float
    READ_PAIRS: float
    PAIR_ORIENTATION: str
    WIDTH_OF_10_PERCENT: float
    WIDTH_OF_20_PERCENT: float
    WIDTH_OF_30_PERCENT: float
    WIDTH_OF_40_PERCENT: float
    WIDTH_OF_50_PERCENT: float
    WIDTH_OF_60_PERCENT: float
    WIDTH_OF_70_PERCENT: float
    WIDTH_OF_80_PERCENT: float
    WIDTH_OF_90_PERCENT: float
    WIDTH_OF_95_PERCENT: float
    WIDTH_OF_99_PERCENT: float
