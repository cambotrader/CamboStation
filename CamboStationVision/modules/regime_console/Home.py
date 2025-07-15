import streamlit as st
from regime_console_core import track_regimes, load_legacy

st.title("📖 Regime Console - Identity Regime")
logs = load_legacy()
if not logs:
    st.error("No legacy data found.")
else:
    for period, label, count in track_regimes(logs):
        st.markdown(f"- {period}: **{label}** ({count} sessions)")
