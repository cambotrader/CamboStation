import streamlit as st
from belief_mutation import belief_codex
st.title("?? Belief Codex Evolution")
for belief in belief_codex:
    st.markdown(f"- {belief}")
