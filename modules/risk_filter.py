import streamlit as st

def apply_filter(mock_vix=32.1, threshold=35):
    if mock_vix >= threshold:
        st.error(f"🛑 VIX = {mock_vix} – Market volatility too high. Execution blocked.")
        return False
    else:
        st.success(f"✅ VIX = {mock_vix} – Safe to execute.")
        return True
