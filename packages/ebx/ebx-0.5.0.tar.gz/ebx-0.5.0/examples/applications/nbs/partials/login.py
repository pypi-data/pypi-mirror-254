import streamlit as st
from helpers.utils import sign_in_with_email_and_password


def login():
    email = st.text_input(label="Email", placeholder="user1@earthblox.io", value="")
    password = st.text_input(label="Password", placeholder="********", type="password", value="")

    if st.button('Sign In'):
        st.write('signing in...')
        user_creds = sign_in_with_email_and_password(email, password)
        st.session_state['token'] = user_creds['idToken']
        st.session_state['refreshToken'] = user_creds['refreshToken']
        st.session_state['expiresIn'] = user_creds['expiresIn']
        st.session_state['localId'] = user_creds['localId']
        st.session_state['user_creds'] = user_creds