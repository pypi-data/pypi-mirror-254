import streamlit as st
from helpers.api import createRun, getStatus, getRun
from components.ebx_map import ebx_map
from components.ebx_table import ebx_table
from components.ebx_figure import ebx_figure
from polling2 import poll


def dashboard(project: dict, fc: dict):
    
    with st.spinner(text="In progress..."):
        projectID = project['id']

        if st.session_state.get('selected_project_id', None) is None:
            st.session_state['selected_project_id'] = projectID
            

        # only create a new run if the project has changed
        if projectID != st.session_state['selected_project_id'] or st.session_state.get('run_id', None) is None:
            st.session_state['selected_project_id'] = projectID
            run_id = createRun(projectID, study_area=fc)
            st.session_state['run_id'] = run_id

        run_id = st.session_state['run_id']

        poll(lambda: getStatus(run_id) == "completed", step = 10, timeout= 300)
        run = getRun(run_id)

        col_1, col_2 = st.columns(2)

        outputs = run.get_outputs()

        with col_1:
            ebx_table(outputs)

        with col_2:
            ebx_figure(outputs)

        layers = run.layers

        ebx_map(layers)
