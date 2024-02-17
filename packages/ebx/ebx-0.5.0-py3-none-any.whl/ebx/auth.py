"""
----------------------------------------------------------------------------
COMMERCIAL IN CONFIDENCE

(c) Copyright Quosient Ltd. All Rights Reserved.

See LICENSE.txt in the repository root.
----------------------------------------------------------------------------
"""
from ebx.models.auth_token import AuthToken
from os import getenv
import httpx
import datetime
import datetime
from ebx.config import ClientConfig
import base64
from abc import ABC
from ebx.constants.api import API_TOKEN_FILE
from typing import Dict

class AbstractAuthentication(ABC):
    """Abstract class for authentication."""

    auth_token: AuthToken
    """The authentication token."""

    config: ClientConfig
    """The client configuration."""

    def __init__(self, config: ClientConfig):
        self.auth_token = None
        self.config = config

    def has_expired(self) -> bool:
        """Returns whether the token has expired."""

        if self.auth_token is None:
            return True
        
        if self.auth_token.expires is None:
            return True
        
        if self.auth_token.expires < datetime.datetime.now(tz=datetime.timezone.utc):
            return True
        
        return False
    
    def refresh(self) -> None:
        """Refreshes the token."""
        pass

    def id(self) -> int:
        """Returns the id of the authentication method."""
        return id(self)
    
    def get_headers(self) -> Dict[str, str]:
        """Returns the headers for the request."""
        return {}

class EnvAuthentication(AbstractAuthentication):
    """Authentication using the EBX_API_TOKEN environment variable."""

    def __init__(self, config: ClientConfig) -> None:
        self.auth_token = getenv("EBX_API_TOKEN")
        self.config = config

    def has_expired(self):
        return False
    
    def refresh(self) -> "EnvAuthentication":
        return self.setToken(getenv("EBX_API_TOKEN"))
    
    def setToken(self, token: str) -> "EnvAuthentication":
        self.auth_token = token
        return self
    
    def get_headers(self) -> Dict[str, str]:
        return {
            "Authorization": f"Bearer {self.auth_token}",
        }
    
class BasicAuth(AbstractAuthentication):
    """Authentication using a username and password."""

    email: str
    """The email address."""

    password: str
    """The password."""

    def __init__(self, config: ClientConfig, email: str, password: str) -> None:
        self.email = email
        self.password = password
        self.config = config

    def has_expired(self) -> bool:
        return False
    
    def refresh(self):
        """BasicAuth does not support refresh"""
        raise NotImplementedError("BasicAuth does not support refresh")
    
    def get_headers(self) -> Dict[str, str]:
        """Returns the basic auth headers."""
        base64string = base64.b64encode(f"{self.email}:{self.password}".encode('utf-8')).decode('utf-8')
        return {
            "Authorization": f"Basic {base64string}",
        }

class OAuthAuthentication(AbstractAuthentication):
    """Authentication using OAuth."""

    client_id: str
    """The client id."""

    client_secret: str
    """The client secret."""

    def __init__(self, config: ClientConfig, client_id: str = None, client_secret: str = None):
        """Authenticates using OAuth, raises error if no client id or secret provided.
        
        Args:
            config (ClientConfig): The client configuration.
            client_id (str): The client id.
            client_secret (str): The client secret.

        Raises:
            ValueError: If no client id or secret provided.
        """
        self.config = config
        self.client_id = client_id
        self.client_secret = client_secret

        if self.client_id is None:
            self.client_id = getenv("EBX_CLIENT_ID")
        if self.client_secret is None:
            self.client_secret = getenv("EBX_CLIENT_SECRET")
        self.auth_token = None

        if self.client_secret is None:
            raise ValueError("No client secret provided")
        if self.client_id is None:
            raise ValueError("No client id provided")
        
        self.load_saved_credentials()

    def refresh(self) -> "OAuthAuthentication":
        """Creates a new token for the client.

        Returns:
            OAuthAuthentication: The authentication object.
        """
        request_data = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }

        headers = {
            'Content-Type': 'application/json'
        }

        res = httpx.post(self.config.get_oauth_url(), json=request_data, headers=headers)

        if res.status_code == 200:
            response_json = res.json()
            expires = datetime.datetime.fromisoformat(response_json["expires"]).replace(tzinfo=datetime.timezone.utc)
            self.auth_token = AuthToken(token=response_json["token"], expires=expires)
            self.save_credentials()
            return self
        else:
            res.raise_for_status()
        
    def get_headers(self):
        return {
            "Authorization": f"Bearer {self.auth_token.token}",
        }
    
    def get_token_filename(self) -> str:
        """Returns the filename for the token."""
        return f"{self.client_id}_{API_TOKEN_FILE}"
    
    def load_saved_credentials(self) -> "OAuthAuthentication":
        """Loads the saved credentials from the file system if they exist."""
        if AuthToken.saved_token_exists(self.config, self.get_token_filename()):
            self.auth_token = AuthToken.load(self.config, self.get_token_filename())

        return self
    
    def save_credentials(self) -> "OAuthAuthentication":
        """Saves the credentials to the file system."""
        self.auth_token.save(self.config, self.get_token_filename())

        return self