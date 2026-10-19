import streamlit as st
from supabase import create_client, Client

SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_SECRET_KEY = st.secrets["SUPABASE_SECRET_KEY"]

supabase: Client = create_client(
    SUPABASE_URL,
    SUPABASE_SECRET_KEY
)
