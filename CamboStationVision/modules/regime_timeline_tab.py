import streamlit as st
from regime_memory import regime_log
st.title("??? Regime Timeline")
for entry in regime_log[-5:]:
    st.markdown(f"- {entry['mood']} | {entry['archetype']} | VIX: {entry['volatility']}")
