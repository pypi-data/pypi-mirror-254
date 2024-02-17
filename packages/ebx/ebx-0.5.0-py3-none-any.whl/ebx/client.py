"""API client for Earth Blox."""

"""
----------------------------------------------------------------------------
COMMERCIAL IN CONFIDENCE

(c) Copyright Quosient Ltd. All Rights Reserved.

See LICENSE.txt in the repository root.
----------------------------------------------------------------------------
"""
import httpx
from contextlib import contextmanager
from ebx.auth import EnvAuthentication, AbstractAuthentication, OAuthAuthentication
from typing import Any
from ebx.config import ClientConfig
from ebx.models.oauth_client import OAuthClient
from ebx.constants.api import API_SECRETS_FILE

class ClientManager():
    """Singleton for managing clients. This is able to keep context of the current client being used. Allows for reuse of the same client in a single context."""
    clients: dict = {}
    endpoints: dict = {}
    _instance: "ClientManager" = None
    current_context: str = None
    previous_context: str = None

    def __new__(cls) -> "ClientManager":
        if cls._instance is None:
            cls._instance = super(ClientManager, cls).__new__(cls)

        return cls._instance

    def set_client(self, *args, **kwargs) -> "Client":
        """Sets the client for the context."""
        if kwargs.get('authenticator') is None:
            raise Exception("Client requires a authenticator")
        
        if kwargs.get('name') is None:
            client_id = kwargs.get('authenticator').id()
        else:
            client_id = kwargs.get('name')

        if self.clients.get(client_id) is None:
            self.clients[client_id] = Client(*args, **kwargs)
        
        return self.clients[client_id]
    
    def register_endpoint(self, func) -> "ClientManager":
        """Registers a function as an api endpoint."""
        self.endpoints[func.__name__] = func
        return self
    
    def set_current_context(self, context: str)  -> "Client":
        """Sets the current context."""
        self.previous_context = self.current_context
        self.current_context = context
        return self
    
    def reset_context(self) -> "ClientManager":
        """Resets the context."""
        self.current_context = self.previous_context
        return self
    
    def get_current_context(self) -> "Client":
        """Gets the current context."""
        return self.current_context
    
    def has_endpoint(self, endpoint: str) -> bool:
        """Checks if the endpoint exists."""
        return endpoint in self.endpoints
    
    def get_endpoint(self, endpoint: str) -> Any:
        """Gets the endpoint."""
        return self.endpoints[endpoint]
    
    def using_no_context(self) -> bool:
        """Checks if the client is being used without a context."""
        return self.current_context is None and self.previous_context is None
    
    def get_first_client(self) -> "Client":
        if len(self.clients) == 0:
            raise Exception("No clients have been created")
        return list(self.clients.values())[0]
    
    def get_client_by_name(self, name) -> "Client":
        if self.clients.get(name) is None:
            raise Exception(f"No client with name {name} has been created")
        return self.clients.get(name)
    
class Client():
    """Earth Blox API client."""

    name: str = None
    """The name of the client."""

    config: ClientConfig = None
    """The api url for the Earth Blox API."""

    authenticator: AbstractAuthentication = None
    """The auth bearer token for the Earth Blox API."""
    
    def __init__(self, authenticator: AbstractAuthentication = None, config: ClientConfig = None, name: str = None):
        """Initialize the client.

        Args:
            authenticator (AbstractAuthentication): Authentication method for the client. Defaults to None.
            config (ClientConfig): The config for the client. Defaults to None.
            name (str): The name of the client. Defaults to None.
        """

        if config is None:
            config = ClientConfig()

        self.config = config
        self.name = name
        
        if authenticator is None:
            authenticator = EnvAuthentication()

        self.authenticator = authenticator
    
    def _get_headers(self) -> dict:
        """Gets the headers for the request, tokens and content type.
        
        Returns
            dict: The headers for the request.
        """
        base_headers = {
            "Content-Type": "application/json",
        }
        auth_headers = self.authenticator.get_headers()
        base_headers.update(auth_headers)
        return base_headers
    
    @contextmanager
    def ebx_client(self,config: ClientConfig = None) -> httpx.Client:
        """Context manager for the httpx client.

        Includes the auth authenticator and content type headers.
        Includes the base url for the Earth Blox API.
        
        Yields:
            httpx.Client: The httpx client.
        """
        if self.authenticator.has_expired():
            self.authenticator = self.authenticator.refresh()
        
        headers = self._get_headers()

        if config is None:
            config = self.config

        with httpx.Client(base_url=config.get_api_base_url(), headers=headers) as client:
            yield client
    
    def get(self, url: str, query_params: dict = None, headers: dict = None, timeout: int = None) -> dict:
        """Makes a httpx GET request to the Earth Blox API.
        
        Args:
            url (str): The url to request. Should be an earth blox endpoint.
            query_params (dict, optional): Query parameters for the request. Defaults to None.
            headers (dict, optional): Headers for the request. Defaults to None.
            timeout (int, optional): Timeout for the request. Defaults to None.

        Returns:
            dict: The response from the request.
        """
        
        query_params = query_params or {}
        headers = headers or {}

        with self.ebx_client() as client:
            response = client.get(url, params=query_params, headers=headers, timeout=timeout)
            response.raise_for_status()
            return response.json()
        
    def post(self, url: str, payload: dict = None, headers: dict = None, timeout: int = None) -> dict:
        """Makes a httpx POST request to the Earth Blox API.
        
        Args:
            url (str): The url to request. Should be an earth blox endpoint.
            payload (dict, optional): Payload for the request. Defaults to None.
            headers (dict, optional): Headers for the request. Defaults to None.
            timeout (int, optional): Timeout for the request. Defaults to None.

        Returns:
            dict: The response from the request.
        """
        payload = payload or {}
        headers = headers or {}
        
        with self.ebx_client() as client:
            response = client.post(url, json=payload, headers=headers, timeout=timeout)
            response.raise_for_status()
            return response.json()
        
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        return self
    
    def __getattr__(self, __name: str) -> Any:
        """Updates the client manager to know the last client used, and gets the endpoint from the client manager to call."""
        clientManager = ClientManager()
        if clientManager.has_endpoint(__name):
            def wrappedContext(*args, **kwargs):
                try:
                    clientManager.set_current_context(self)
                    result = clientManager.get_endpoint(__name)(*args, **kwargs)
                    return result
                finally:
                    clientManager.reset_context()
            return wrappedContext
        return super().__getattr__(__name)
    
    def __str__(self) -> str:
        return f"Client(name={self.name}, config={self.config}, authenticator={self.authenticator})"

def register_endpoint():
    """registers a function as an api endpoint"""
    def decorator(func):
        ClientManager().register_endpoint(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator
    
def get_client(name=None) -> Client:
    """Gets the first relevant client.

    Client is either the client by name, the first client or the current context (the last one used).
    
    Returns:
        Client: The client api.
    """
    client = None

    if name is not None:
        client = ClientManager().get_client_by_name(name)
    elif ClientManager().using_no_context():
        client = ClientManager().get_first_client()
    else:
        client = ClientManager().get_current_context()

    return client

def auth_using(authenticator: AbstractAuthentication, config: ClientConfig = None, name: str = None) -> Client:
    """Authenticates the client using the client id and secret.
    
    Args:
        client_id (str): The client id.
        client_secret (str): The client secret.
    
    Returns:
        Client: The client api.
    """
    if config is None:
        config = ClientConfig()

    kwargs = {
        'authenticator': authenticator,
        'config': config
    }

    manager = ClientManager()

    client = manager.set_client(name=name, **kwargs)

    # update the client manager context assuming that the user is likely to want to use this client next after authenticating
    # this is particularly important if the user has used a service client last to create some credentials
    manager.set_current_context(client)

    return client

def auth_using_env(name: str = None, config: ClientConfig = None) -> Client:
    """Authenticates the client using the environment variables.
    Args:
        name (str): The name of the client.
        config (ClientConfig): The config for the client. Defaults to None.

    Returns:
        Client: The client api.
    """
    if config is None:
        config = ClientConfig()
    return auth_using(EnvAuthentication(config), name=name)

def auth_using_oauth(client_id: str = None, client_secret: str = None, name: str = None, config: ClientConfig = None) -> Client:
    """Authenticates the client using the client id and secret.
    
    Args:
        client_id (str): The client id.
        client_secret (str): The client secret.
        name (str): The name of the client.
        config (ClientConfig): The config for the client. Defaults to None.
    
    Returns:
        Client: The client api.
    """
    if config is None:
        config = ClientConfig()

    return auth_using(OAuthAuthentication(config, client_id, client_secret), name=name)

def auth_using_creds(filename: str=API_SECRETS_FILE, name: str = None, config: ClientConfig = None)-> Client:
    """Authenticates the client using the client id and secret. thats saved to disk

    Args:
        filename (str): The filename of the credentials file.
        path (str): The path of the credentials file.
        name (str): The name of the client.
        config (ClientConfig): The config for the client. Defaults to None.

    Returns:
        Client: The client api.
    """
    if config is None:
        config = ClientConfig()

    oauthClient = OAuthClient.load(config=config, filename=filename)
    client_id = oauthClient.client_id
    client_secret = oauthClient.client_secret

    return auth_using(OAuthAuthentication(config, client_id, client_secret), name=name)