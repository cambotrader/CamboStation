import streamlit as st
import pandas as pd
import plotly.graph_objs as go
from datetime import datetime
import os

logbook_path = "logs/pattern_log.csv"

# ─────────────────────────────────────────────
# Logging function
# ─────────────────────────────────────────────
def log_pattern(pattern_name, date, chart_data, commentary, outcome="Pending"):
    log_entry = {
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Pattern": pattern_name,
        "DetectionDate": pd.to_datetime(date).strftime("%Y-%m-%d"),

        "Commentary": commentary,
        "Outcome": outcome
    }
    df = pd.DataFrame([log_entry])

    if not os.path.exists("logs"):
        os.makedirs("logs")

    if os.path.exists(logbook_path):
        df.to_csv(logbook_path, mode="a", header=False, index=False)
    else:
        df.to_csv(logbook_path, index=False)

# ─────────────────────────────────────────────
# Viewer function
# ─────────────────────────────────────────────
def render_logbook_viewer():
    st.subheader("✍️ Pattern Intelligence Logbook")

    if not os.path.exists(logbook_path):
        st.warning("🗂 No pattern logs found yet.")
        return

    df = pd.read_csv(logbook_path)
    st.dataframe(df.tail(20), use_container_width=True)

    st.download_button(
        label="📄 Download Full Logbook (CSV)",
        data=df.to_csv(index=False).encode(),
        file_name="pattern_logbook.csv",
        mime="text/csv"
    )

    st.caption("🧠 Tactical logbook — archives detected patterns with commentary and outcomes.")
