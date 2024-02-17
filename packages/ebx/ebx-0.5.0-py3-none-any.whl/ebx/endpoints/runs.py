"""Defines the runs endpoints."""

"""
----------------------------------------------------------------------------
COMMERCIAL IN CONFIDENCE

(c) Copyright Quosient Ltd. All Rights Reserved.

See LICENSE.txt in the repository root.
----------------------------------------------------------------------------
"""
from ebx.client import get_client, register_endpoint
from ebx.models.project_spec import ProjectSpecType, StudyArea
from ebx.models.run import Run
from typing import List, Union
from datetime import datetime

@register_endpoint()
def list_runs(limit: int = 10) -> List[Run]:
    """Lists the runs.

    Args:
        limit (int, optional): The number of runs to return. Defaults to 10.

    Returns:
        Run List: The list of runs.
    """
    client = get_client()

    params = {
        "limit": limit
    }

    res = client.get("/runs/", query_params=params)

    return [Run(**run) for run in res.get("runs")]

@register_endpoint()
def get_run(run_id: str) -> Run:
    """Gets a specified run by id.
    
    Args:
        run_id (str): The id of the run.

    Returns:
        Run: The run.
    """
    client = get_client()

    res = client.get(f"/runs/{run_id}")
    
    return Run(**res)

@register_endpoint()
def get_run_status(run_id: str) -> str:
    """Gets the current status of a run.
    
    Args:
        run_id (str): The id of the run.

    Returns:
        The run status.
    """

    client = get_client()

    res = client.get(f"/runs/{run_id}/status")
    
    return res.get("status")

# create run makes post request to /runs
# returns run id
# TODO: update to work with href method
@register_endpoint()
def create_run(
        project_id: str, 
        start_date: Union[datetime, str] = None,
        end_date: Union[datetime, str] = None,
        study_area: StudyArea = None,
        include_geometry: bool = False,
        generate_thumbnails: bool = False,
        ) -> str:
    """Creates a run using the specified project.
    
    Args:
        project_id (str): The id of the project to use.
        start_date (Union[datetime, str], optional): The start date of datasets in the run. Defaults to None.
        end_date (Union[datetime, str], optional): The end date of datasets in the run. Defaults to None.
        study_area (StudyArea, optional): The study area of the run. Defaults to None.
        include_geometry (bool, optional): Whether to include geometry in the output of tabular data. Defaults to False.
        generate_thumbnails (bool, optional): Whether to generate thumbnails for every layer in the run. Defaults to False.

    Returns:
        str: The id of the run.
    """

    client = get_client()

    has_params = any([start_date, end_date, study_area])

    substitutions = {}

    if not isinstance(include_geometry, bool):
        raise TypeError("include_geometry must be a boolean.")
    
    if not isinstance(generate_thumbnails, bool):
        raise TypeError("generate_thumbnails must be a boolean.")

    body = {
        "type": ProjectSpecType.TEMPLATE.value,
        "project_id": project_id,
        "include_geometry": include_geometry,
        "generate_thumbnails": generate_thumbnails
    }

    # TODO: add conversion of start and end date to string

    if has_params:
        substitutions = {}

        if start_date and end_date:
            date_range = {
                "start_date": start_date,
                "end_date": end_date,
            }

            substitutions["date_range"] = date_range

        elif (start_date is None) ^ (end_date is None):
            raise ValueError("Both start_date and end_date must be specified if either is specified.")


        if study_area:
            substitutions["study_area"] = study_area

        body["substitutions"] = substitutions

    res = client.post("/runs/", body)
    
    return res.get("run_id")

@register_endpoint()
def follow_run(run_id: str) -> Run:
    """Follows a run until it is complete, or after 5 minutes.
    
    Args:
        run_id (str): The id of the run.
        
    Returns:
        Run: The run.

    Raises:
        Exception: If the run is not complete after 5 minutes.
    """
    # create a poller to continuously poll the run using get_run with status only

    # if the run is complete, return the run

    # if the run is not complete after 5 minutes, raise an exception

    raise NotImplementedError