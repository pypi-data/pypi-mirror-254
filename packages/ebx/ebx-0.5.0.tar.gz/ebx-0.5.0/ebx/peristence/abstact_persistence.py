"""
----------------------------------------------------------------------------
COMMERCIAL IN CONFIDENCE

(c) Copyright Quosient Ltd. All Rights Reserved.

See LICENSE.txt in the repository root.
----------------------------------------------------------------------------
"""
from abc import ABC
class AbstractPersistence(ABC):
    """Abstract class for persistence."""
    def save(self, key: str, data):
        """Save data to persistence.

        Args:
            key (str): Key to save data under.
            data (Any): Data to save.

        Returns:
            AbstractPersistence: Self.
        """
        raise NotImplementedError()

    def load(self, key: str):
        """Load data from persistence.

        Args:
            key (str): Key to save data under.

        Returns:
            AbstractPersistence: Self.
        """
        raise NotImplementedError()
    
    def exists(self, key: str) ->bool:
        """Check if data exists in persistence.

        Args:
            key (str): Key to save data under.

        Returns:
            bool: Whether data exists.
        """
        raise NotImplementedError()
    
    def set_path(self, path: str):
        """Set the path for persistence.

        Args:
            path (str): Path to save data under.

        Returns:
        AbstractPersistence: Self.
        """
        raise NotImplementedError()