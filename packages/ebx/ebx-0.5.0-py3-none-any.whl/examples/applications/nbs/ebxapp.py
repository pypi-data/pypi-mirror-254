import streamlit as st
from partials.login import login
from partials.projects import projects
from partials.dashboard import dashboard
from partials.polygon_upload import upload_polygons
from helpers.utils import isLoggedIn

st.set_page_config(layout="wide")
st.title('EBX App')

if isLoggedIn():
    project = st.session_state.get('project', None) or projects()
    st.session_state['project'] = project

    if project is not None and st.session_state.get('fc', None) is None:
        fc = upload_polygons()
        st.session_state['fc'] = fc

    fc = st.session_state.get('fc', None)

    if project and fc:
        dashboard(project, fc)

else:
    login()
    if isLoggedIn():
        st.experimental_rerun()
        
    
