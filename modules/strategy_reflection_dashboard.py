import streamlit as st
from forecast_dreams import recall_dreams

st.title("?? Strategy Dream Reflection")
dreams = recall_dreams()
for d in dreams:
    st.markdown(f"- {d['timestamp']} | Archetype: {d['archetype']} | Mood: {d['mood']} | Signal: {d['signal']}")
