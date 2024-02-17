"""The Earth Blox client library"""

"""
----------------------------------------------------------------------------
COMMERCIAL IN CONFIDENCE

(c) Copyright Quosient Ltd. All Rights Reserved.

See LICENSE.txt in the repository root.
----------------------------------------------------------------------------
"""

__version__ = "0.5.0"

from ebx.endpoints.runs import list_runs, get_run, follow_run, create_run, get_run_status
from ebx.endpoints.projects import list_projects, get_project

from ebx.client import auth_using, auth_using_oauth, auth_using_env, auth_using_creds, register_endpoint, get_client
from ebx.endpoints.services import create_oauth_client
from ebx.config import ClientConfig