"""Class defining a project."""

"""
----------------------------------------------------------------------------
COMMERCIAL IN CONFIDENCE

(c) Copyright Quosient Ltd. All Rights Reserved.

See LICENSE.txt in the repository root.
----------------------------------------------------------------------------
"""
from dataclasses import dataclass

@dataclass
class Project:
    """Describes a project."""

    id: str
    """The id of the project."""

    name: str
    """The name of the project."""

    description: str = None
    """The description of the project."""

    version: str = None
    """The valid API version for the project."""