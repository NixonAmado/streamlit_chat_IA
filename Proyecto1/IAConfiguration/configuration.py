import streamlit as st
from huggingface_hub import InferenceClient
# Obtener el token
api_key = st.secrets["inference"]["token"]
client = InferenceClient(api_key=api_key)

