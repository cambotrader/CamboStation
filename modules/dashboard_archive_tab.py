from session_poetry_index import build_poetry_index
import streamlit as st

def render_archive_tab():
    st.title("🪶 Voice Memory Stream")
    st.markdown("### Session Poetry Index")
    for line in build_poetry_index():
        st.markdown(line)
    st.markdown("📁 Voice archives saved as `voice_archive_YYYY-MM-DD_HH-MM.txt`")
