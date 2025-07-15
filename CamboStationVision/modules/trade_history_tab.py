import streamlit as st
import json, os

def render():
    st.subheader("📊 Trade History Replay")

    log_file = os.path.join(os.path.dirname(__file__), "..", "logs", "voting_history.json")
    if not os.path.exists(log_file):
        st.info("No trade history found yet.")
        return

    with open(log_file, "r", encoding="utf-8") as f:
        history = json.load(f)

    for entry in reversed(history[-25:]):  # Show last 25 entries
        st.markdown(f"**{entry['timestamp']}** — `{entry['asset'].upper()}` → `{entry['signal'].upper()}` ({entry['confidence']}) → `{entry['outcome']}`")
