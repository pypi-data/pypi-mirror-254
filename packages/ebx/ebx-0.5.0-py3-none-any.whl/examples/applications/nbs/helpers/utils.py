import json
import requests
from helpers.config import FIREBASE_WEB_API_KEY
import streamlit as st


def sign_in_with_email_and_password(email, password, return_secure_token=True):
    payload = json.dumps({"email":email, "password":password, "return_secure_token":return_secure_token})
    
    rest_api_url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"

    r = requests.post(rest_api_url,
                  params={"key": FIREBASE_WEB_API_KEY},
                  data=payload)

    return r.json()

def isLoggedIn():
    return 'token' in st.session_state and st.session_state['token'] is not None

def getUserToken():
    return st.session_state['token'] if isLoggedIn() else None