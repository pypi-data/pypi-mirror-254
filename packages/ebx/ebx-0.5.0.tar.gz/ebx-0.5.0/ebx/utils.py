"""Utils for making Earth Blox API requests."""

"""
----------------------------------------------------------------------------
COMMERCIAL IN CONFIDENCE

(c) Copyright Quosient Ltd. All Rights Reserved.

See LICENSE.txt in the repository root.
----------------------------------------------------------------------------
"""
from ebx.encoder import PlotlyJSONEncoder as JSONEncoder
from typing import Any
import json

def serialize(data: Any) -> str:
    """Serialize data to json.
    
    Args:
        data (Any): Data to serialize.

    Returns:
        str: Serialized data.
    """

    return json.dumps(data, cls=JSONEncoder)