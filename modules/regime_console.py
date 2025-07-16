# -*- coding: utf-8 -*-
import streamlit as st
import os, json
from collections import defaultdict, Counter
from datetime import datetime
import pandas as pd
import talib

# Optional: import PatternPy if installed
try:
    from patternpy.tradingpatterns import head_and_shoulders
except ImportError:
    head_and_shoulders = None

# Identity consistency score calculator
try:
    from identity_consistency_score import compute_consistency_score
except Exception:
    compute_consistency_score = None

# ────────────────────────────────
# 🔍 Legacy data loader
def load_legacy():
    path = os.path.join(os.path.expanduser("~"), "CamboStation_QuantumOS", "modules", "myth_legacy.json")
    if not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

# 📅 Date formatter
def get_period(date_str):
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    return dt.strftime("%Y-%m")

# 📊 Monthly regime tracker
def track_regimes(logs):
    by_period = defaultdict(list)
    for date, entry in logs.items():
        parts = entry.split("'")
        if len(parts) < 4:
            continue
        label = f"{parts[1]}:{parts[3]}"
        period = get_period(date)
        by_period[period].append(label)
    results = []
    for period in sorted(by_period):
        freq = Counter(by_period[period])
        top = freq.most_common(1)[0]
        results.append((period, top[0], top[1]))
    return results

# 🧪 Sample OHLC for pattern recognition
def load_sample_ohlc():
    dates = pd.date_range(end=datetime.today(), periods=50)
    data = pd.DataFrame({
        "Open": pd.Series([100 + i + (i % 5) * 2 for i in range(50)], index=dates),
        "High": pd.Series([102 + i + (i % 3) * 2 for i in range(50)], index=dates),
        "Low": pd.Series([98 + i - (i % 4) * 2 for i in range(50)], index=dates),
        "Close": pd.Series([101 + i + (i % 2) * 2 for i in range(50)], index=dates),
    })
    return data

# 🧠 Main dashboard
def render_dashboard():
    st.set_page_config(layout="wide")
    st.title("📖 CamboStation Regime Console")

    tabs = st.tabs([
        "🧭 Identity Regime",
        "🧩 Consistency Score",
        "📈 Candlestick Patterns",
        "🗺️ Chart Patterns"
    ])

    with tabs[0]:
        st.header("🧭 Dominant Regimes by Month")
        logs = load_legacy()
        if not logs:
            st.error("No legacy data found.")
        else:
            for period, label, count in track_regimes(logs):
                st.markdown(f"- {period}: **{label}** ({count} sessions)")

    with tabs[1]:
        st.header("🧩 Identity Consistency Score")
        if compute