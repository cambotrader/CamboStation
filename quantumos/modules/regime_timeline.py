import streamlit as st
from regime_memory import regime_log
st.title("??? Regime Timeline")
for entry in regime_log[-5:]:
    st.markdown(f"- Mood: **{entry['mood']}**, Archetype: **{entry['archetype']}**, Volatility: {entry['volatility']}")
