"""Class defining a oauth client."""

"""
----------------------------------------------------------------------------
COMMERCIAL IN CONFIDENCE

(c) Copyright Quosient Ltd. All Rights Reserved.

See LICENSE.txt in the repository root.
----------------------------------------------------------------------------
"""
from dataclasses import dataclass,asdict
from ebx.constants.api import API_SECRETS_FILE
from ebx.config import ClientConfig, ServiceClientConfig

@dataclass
class OAuthClient:
    """Describes a oauth client."""

    name: str
    """The id of the client."""

    description: str
    """The description of the client."""

    client_id: str
    """The Client ID of the client."""

    client_secret: str
    """The Client secret."""

    enabled: bool
    """Whether the client is enabled."""

    def save(self, config: ClientConfig = None, filename: str = API_SECRETS_FILE) -> 'OAuthClient':
        """Save this dataclass to disk in json format

        Args:
            config (ClientConfig, optional): The client config. Defaults to None.
            filename (str, optional): The filename. Defaults to API_SECRETS_FILE.

        Returns:
            OAuthClient: The saved client.
        """
        if config is None:
            config = ServiceClientConfig()

        config.get_persistence_driver().save(filename, asdict(self))
        return self

    @staticmethod
    def load(config: ClientConfig = None, filename: str = API_SECRETS_FILE) -> 'OAuthClient':
        """Load this dataclass from disk
        
        Args:
            config (ClientConfig, optional): The client config. Defaults to None.
            filename (str, optional): The filename. Defaults to API_SECRETS_FILE.

        Returns:
            OAuthClient: The loaded client.
        """
        if config is None:
            config = ServiceClientConfig()

        data = config.get_persistence_driver().load(filename)
        return OAuthClient(**data)
    
    @staticmethod
    def saved_credentials_exists(config: ClientConfig = None, filename: str = API_SECRETS_FILE) -> bool:
        """Check if a credentials file exists at the given path
        
        Args:
            config (ClientConfig, optional): The client config. Defaults to None.
            filename (str, optional): The filename. Defaults to API_SECRETS_FILE.

        Returns:
            bool: Whether the file exist
        """
        if config is None:
            config = ServiceClientConfig()

        return config.get_persistence_driver().exists(filename)