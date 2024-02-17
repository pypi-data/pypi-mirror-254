"""Defines a layer from earth blox."""

"""
----------------------------------------------------------------------------
COMMERCIAL IN CONFIDENCE

(c) Copyright Quosient Ltd. All Rights Reserved.

See LICENSE.txt in the repository root.
----------------------------------------------------------------------------
"""

from dataclasses import dataclass
from typing import List, Optional

@dataclass
class LayerTimePeriod:
    """Layer groups containing map urls, labels and thumbnails."""
    mapURL: str
    label: str
    thumbnailURL: Optional[str] = None

@dataclass
class Bounds:
    """Defines a bounding box."""
    SW: List[float]
    NE: List[float]

@dataclass
class Legend:
    """Defines a legend for a layer."""
    type: str
    values: List[dict]

@dataclass
class Layer:
    """Defines a layer from earth blox."""
    type: str
    name: str
    time_periods: List[LayerTimePeriod]
    bbox: Bounds
    legend: Optional[Legend] = None

    def __post_init__(self):
        """Convert params to correct classes"""

        self.time_periods = list(map(lambda x: x if isinstance(x, LayerTimePeriod) else LayerTimePeriod(**x), self.time_periods))

        if not isinstance(self.bbox, Bounds):
            self.bbox = Bounds(**self.bbox)

        if self.legend is not None:
            self.legend = Legend(**self.legend)
