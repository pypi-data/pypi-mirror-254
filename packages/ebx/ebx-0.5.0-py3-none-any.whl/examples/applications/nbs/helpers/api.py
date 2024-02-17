
from os import environ
from helpers.utils import getUserToken
import streamlit as st
from dataclasses import asdict
import ebx

@st.cache_data
def getProjects():
    environ["EBX_API_TOKEN"] = getUserToken()
    projects = ebx.list_projects()
    return [asdict(project) for project in projects]


def getProject(id):
    environ["EBX_API_TOKEN"] = getUserToken()
    return ebx.get_project(id)

def createRun(id, start_date=None, end_date=None, study_area=None):
    environ["EBX_API_TOKEN"] = getUserToken()
    return ebx.create_run(id, **{
        "start_date": start_date,
        "end_date": end_date,
        "study_area": study_area
    })

def getStatus(id):
    environ["EBX_API_TOKEN"] = getUserToken()
    return ebx.get_run_status(id)

def getRun(id):
    environ["EBX_API_TOKEN"] = getUserToken()
    return ebx.get_run(id)