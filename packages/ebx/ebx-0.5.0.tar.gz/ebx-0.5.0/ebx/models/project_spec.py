"""Defines the project specification used to create runs from projects."""

"""
----------------------------------------------------------------------------
COMMERCIAL IN CONFIDENCE

(c) Copyright Quosient Ltd. All Rights Reserved.

See LICENSE.txt in the repository root.
----------------------------------------------------------------------------
"""
from geojson_pydantic import Feature, Polygon, MultiPolygon, FeatureCollection
from typing import Dict, Union 
from enum import Enum

class ProjectSpecType(str, Enum):
    """The type of project spec."""
    TEMPLATE = 'template'
    href_TEMPLATE = 'href_template'
    # INLINE = 'inline' # not yet supported

# see https://developmentseed.org/geojson-pydantic/intro/#advanced-usage
PolygonFeature = Feature[Polygon, Dict]
"""A feature that only allows polygon geometry."""

MultiPolygonFeature = Feature[MultiPolygon, Dict]
"""A feature that only allows multi polygon geometry."""

PolygonFeatureCollection = FeatureCollection[Union[PolygonFeature, MultiPolygonFeature]]
"""A feature collection that only allows polygon or multi polygon features."""

StudyArea = Union[PolygonFeatureCollection, PolygonFeature, MultiPolygonFeature]
"""Study area is defined as a polygon feature collection, polygon feature or multi polygon feature.

Feature collections are converted to collections of areas and shapes.

Areas are made up of either a single polygon (A polygon feature) or multiple polygons (A multi polygon feature).
"""