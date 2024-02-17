from partials.upload import upload
from streamlit_extras.switch_page_button import switch_page
import streamlit as st


uploaded = upload()
if uploaded:
    next_page = st.button("Next")
    if next_page:
        switch_page("area")