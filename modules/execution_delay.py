import streamlit as st
import time

def apply_delay(seconds=3):
    with st.spinner(f"⏳ Waiting {seconds}s before execution..."):
        time.sleep(seconds)
    st.success("⏱️ Delay complete – proceeding with execution.")
