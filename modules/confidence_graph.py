import streamlit as st
import json, os
import pandas as pd

def render():
    st.subheader("📈 Signal Confidence Over Time")
    log_file = os.path.join(os.path.dirname(__file__), "..", "logs", "voting_history.json")
    if not os.path.exists(log_file):
        st.info("No data found.")
        return

    with open(log_file, "r", encoding="utf-8") as f:
        history = json.load(f)

    df = pd.DataFrame(history)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    st.line_chart(df.set_index("timestamp")["confidence"])
