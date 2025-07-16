import os
os.makedirs("data", exist_ok=True)  # 🔒 Ensures 'data' folder exists
import streamlit as st
from datetime import datetime
import pandas as pd

# 🧠 Strategy Lab Entry Form
def render_strategy_lab():
    st.subheader("🧠 Strategy Lab")

    # 🧩 Strategy Selection
    strategies = ["Breakout Pullback", "Moving Average Bounce", "VWAP Reversal", "News Catalyst Play"]
    selected_strategy = st.selectbox("📈 Select Strategy", strategies)

    # 🧪 Pattern Selection
    patterns = ["Bullish Engulfing", "Double Bottom", "Flag", "Doji", "Triangle"]
    detected_pattern = st.selectbox("🔍 Pattern Detected", patterns)

    # 📌 Outcome Tagging
    st.subheader("📌 Tag Signal Outcome")
    outcome = st.selectbox("🎯 Outcome", ["Target Hit", "Stopped Out", "Neutral", "Pending"])
    impact = st.radio("📊 Impact Rating", ["Low", "Medium", "High"])
    follow_up = st.text_area("🗂️ Follow-through Notes", placeholder="Add trailing logic, confluence, volume cues…")

    # 🗒️ Comment
    user_comment = st.text_area("📝 Strategy Commentary", placeholder="Why you applied this setup?")

    # 💾 Save Entry
    if st.button("✅ Submit Signal"):
        signal_entry = {
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Strategy": selected_strategy,
            "Pattern": detected_pattern,
            "Outcome": outcome,
            "Impact": impact,
            "FollowThrough": follow_up,
            "Comment": user_comment
        }

        try:
            df_existing = pd.read_csv("data/strategy_log.csv")
            df_new = pd.DataFrame([signal_entry])
            df_combined = pd.concat([df_existing, df_new], ignore_index=True)
            df_combined.to_csv("data/strategy_log.csv", index=False)
        except FileNotFoundError:
            df_new = pd.DataFrame([signal_entry])
            df_new.to_csv("data/strategy_log.csv", index=False)

        st.success("📍 Signal Logged Successfully")

    # 📊 Display Logged Entries
    if st.checkbox("📂 View Strategy Log"):
        try:
            log_df = pd.read_csv("data/strategy_log.csv")
            st.dataframe(log_df.tail(10))
        except FileNotFoundError:
            st.warning("🛑 No strategy log found yet.")
