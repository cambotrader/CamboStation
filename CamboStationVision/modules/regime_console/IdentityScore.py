import streamlit as st
try:
    from identity_consistency_score import compute_consistency_score
    score = compute_consistency_score()
    st.title("🧩 Identity Consistency Score")
    st.code(score, language="text")
except Exception as e:
    st.warning("Consistency score module missing or failed to load.")
