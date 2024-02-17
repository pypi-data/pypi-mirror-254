from partials.area import area
from streamlit_extras.switch_page_button import switch_page
import streamlit as st
from partials.dashboard import dashboard
areaChosen = area()
if areaChosen:
    next_page = st.button("Next")
    if next_page:
        #switch_page("area")
        dashboard()

