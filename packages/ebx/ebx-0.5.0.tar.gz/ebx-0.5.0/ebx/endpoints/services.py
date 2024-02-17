"""Defines the projects endpoints."""

"""
----------------------------------------------------------------------------
COMMERCIAL IN CONFIDENCE

(c) Copyright Quosient Ltd. All Rights Reserved.

See LICENSE.txt in the repository root.
----------------------------------------------------------------------------
"""
from typing import List
from ebx.config import ServiceClientConfig
from ebx.auth import BasicAuth
from ebx.client import auth_using
from ebx.constants.api import CLIENT_REGISTRATION_PATH
from ebx.models.oauth_client import OAuthClient

def create_oauth_client(email: str, password: str, name: str, description: str = '', scopes: List[str] = []) -> OAuthClient:
    """Create a new OAuth client.

    Returns:
        OAuthClient: The new OAuth client.
    """
    config = ServiceClientConfig()
    authenticator = BasicAuth(config, email, password)
    client = auth_using(authenticator, config=config)
    payload = {
        'name': name,
        'description': description,
        'scopes': scopes
    }
    res = client.post(CLIENT_REGISTRATION_PATH, payload=payload)
    
    return OAuthClient(**res.get('data'))