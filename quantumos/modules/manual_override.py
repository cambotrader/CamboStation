import streamlit as st

def render():
    st.subheader("🧠 Manual Override Panel")

    force_execute = st.checkbox("Force Execution (Override Filters)")
    if force_execute:
        st.warning("⚠️ Filters bypassed. Signal will trigger regardless of consensus or confidence.")
    else:
        st.info("Execution only occurs if signal meets system requirements.")
