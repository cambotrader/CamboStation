import streamlit as st
import os, json
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from hmmlearn import hmm

# Optional: import broker feed (mocked here)
def load_broker_data():
    dates = pd.date_range(end=datetime.today(), periods=50)
    prices = pd.Series([100 + np.sin(i/5)*10 + np.random.randn()*2 for i in range(50)], index=dates)
    df = pd.DataFrame({ "Close": prices })
    return df

def load_legacy():
    path = os.path.join(os.path.expanduser("~"), "CamboStation_QuantumOS", "modules", "myth_legacy.json")
    if not os.path.exists(path): return {}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def extract_moods(logs):
    moods = []
    for entry in logs.values():
        parts = entry.split("'")
        if len(parts) >= 4:
            moods.append(parts[3])
    return moods

def encode_moods(moods):
    unique = sorted(set(moods))
    mapping = {m: i for i, m in enumerate(unique)}
    return np.array([mapping[m] for m in moods]), mapping

def forecast_mood(moods):
    if len(moods) < 5: return "Insufficient data"
    X, mapping = encode_moods(moods)
    model = hmm.MultinomialHMM(n_components=3, n_iter=100)
    model.fit(X.reshape(-1, 1))
    next_state = model.predict(X.reshape(-1, 1))[-1]
    probs = model.transmat_[next_state]
    forecast = np.argmax(probs)
    inv_map = {v: k for k, v in mapping.items()}
    return f"Next dominant mood likely: {inv_map.get(forecast, 'Unknown')}"

def render_dashboard():
    st.set_page_config(layout="wide")
    st.title("ðŸ”® CamboStation Regime Forecaster")

    tabs = st.tabs(["ðŸ§  Tonal Shift Forecast", "ðŸ“ˆ Broker Feed Sync", "ðŸ“Š Emotional Drift Projection"])

    with tabs[0]:
        st.header("ðŸ§  Forecast Next Mood Regime")
        logs = load_legacy()
        moods = extract_moods(logs)
        result = forecast_mood(moods)
        st.success(result)

    with tabs[1]:
        st.header("ðŸ“ˆ Broker Feed (Mocked)")
        df = load_broker_data()
        st.line_chart(df["Close"])

    with tabs[2]:
        st.header("ðŸ“Š Emotional Drift Projection")
        st.markdown(f"- Total sessions: **{len(moods)}**")
        st.markdown(f"- Unique moods: **{len(set(moods))}**")
        st.markdown(f"- Recent mood: **{moods[-1] if moods else 'N/A'}**")

render_dashboard()
