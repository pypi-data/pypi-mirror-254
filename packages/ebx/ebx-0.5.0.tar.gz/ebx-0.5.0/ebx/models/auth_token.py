"""Class defining a project."""

"""
----------------------------------------------------------------------------
COMMERCIAL IN CONFIDENCE

(c) Copyright Quosient Ltd. All Rights Reserved.

See LICENSE.txt in the repository root.
----------------------------------------------------------------------------
"""
from dataclasses import dataclass, asdict
import datetime
from ebx.constants.api import API_TOKEN_FILE
from ebx.config import ClientConfig

@dataclass
class AuthToken:
    """Holds the authentication for a project."""

    token: str
    """the oauth token for the api"""

    expires: datetime.datetime = None
    """expiration date for the token"""

    def save(self, config:ClientConfig, filename: str=API_TOKEN_FILE):
        """save this dataclass to disk in json format"""
        saveData = asdict(self)
        saveData["expires"] = saveData["expires"].isoformat()
        config.get_persistence_driver().save(filename, saveData)
        return self

    @staticmethod
    def load(config:ClientConfig, filename: str=API_TOKEN_FILE):
        """load this dataclass from disk in json format"""
        data = config.get_persistence_driver().load(filename)
        data["expires"] = datetime.datetime.fromisoformat(data["expires"])
        return AuthToken(**data)
    
    @staticmethod
    def saved_token_exists(config:ClientConfig, filename: str=API_TOKEN_FILE):
        """check if the token file exists"""
        return config.get_persistence_driver().exists(filename)