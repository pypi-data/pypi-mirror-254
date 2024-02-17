"""Constants for the Earth Blox API."""

"""
----------------------------------------------------------------------------
COMMERCIAL IN CONFIDENCE

(c) Copyright Quosient Ltd. All Rights Reserved.

See LICENSE.txt in the repository root.
----------------------------------------------------------------------------
"""

BASE_URL: str = "https://api.earthblox.io"
"""Base url for the Earth Blox API."""

VERSION: str = "v1beta"
"""Default version prefix for all calls"""

OAUTH_PATH: str = "/services/oauth/token/"
"""The url for the oauth client_credentials flow."""

CLIENT_REGISTRATION_PATH: str = "/services/auth/client/"
"""The url for the client registration url"""

API_PREFIX: str = f"/{VERSION}"
"""The prefix for the Earth Blox API."""

API_SECRETS_FILE: str = ".ebx.auth.json"
"""The file name for the api secrets file."""

API_SECRETS_PATH: str = "./.ebx/"
"""The path for the api secrets file."""

API_TOKEN_FILE: str = ".ebx.token.json"
"""The file name for the api token file."""