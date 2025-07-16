import streamlit as st
from signal_persona_grid import get_grid
from invocation_engine import invoke_market_identity

st.title("?? Strategic Identity Log")
grid = get_grid()
for entry in grid:
    st.markdown(f"- Signal: **{entry['signal']}** | Mood: {entry['mood']} | Archetype: {entry['archetype']} | Belief: {entry['belief']}")
st.divider()
st.write(invoke_market_identity("reflective", "Oracle"))
