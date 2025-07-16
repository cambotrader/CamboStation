import streamlit as st
import os, json
from collections import defaultdict, Counter
from datetime import datetime
from identity_consistency_score import compute_consistency_score

def load_legacy():
    path = os.path.join(os.path.expanduser("~"), "CamboStation_QuantumOS", "modules", "myth_legacy.json")
    if not os.path.exists(path): return {}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def get_period(date_str):
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    return dt.strftime("%Y-%m")

def track_regimes(logs):
    by_period = defaultdict(list)
    for date, entry in logs.items():
        parts = entry.split("'")
        if len(parts) < 4: continue
        label = f"{parts[1]}:{parts[3]}"
        period = get_period(date)
        by_period[period].append(label)
    results = []
    for period in sorted(by_period):
        freq = Counter(by_period[period])
        top = freq.most_common(1)[0]
        results.append((period, top[0], top[1]))
    return results

def render_dashboard():
    st.set_page_config(layout="wide")
    st.title("📊 Identity Regime & Consistency Panel")

    logs = load_legacy()
    if not logs:
        st.error("No legacy data found.")
        return

    # 🔮 Regime Tracking
    st.markdown("### 🔮 Dominant Regimes by Month")
    for period, label, count in track_regimes(logs):
        st.markdown(f"- {period}: **{label}** ({count} sessions)")

    # 🧠 Consistency Score
    st.markdown("### 🧠 Identity Consistency Score")
    st.code(compute_consistency_score(), language="text")

render_dashboard()
