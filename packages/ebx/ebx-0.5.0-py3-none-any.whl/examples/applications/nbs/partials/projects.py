"""Creates a list of NBS projects available to the user, shows them and allows them to choose them to run."""

import streamlit as st
from helpers.api import getProjects

def projects() -> dict:
    content = 'projects'
    st.session_state['content_category'] = content
    st.write(st.session_state['content_category'])

    container = st.container()
    with container:
        projects_list = getProjects()

        # filter for projects starting with 'NbS:
        projects_list = [project for project in projects_list if project['name'].startswith('NbS:')]

        # create a dropdown list of projects
        project = st.selectbox('Select a project', projects_list, format_func=lambda project: project['name'])

        button_name = f"Run {project['name']}"

        # create a button to run the project
        if st.button(button_name):
            # navigate to page to run project
            return project