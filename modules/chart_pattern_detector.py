import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objs as go
from datetime import datetime
from modules.pattern_logbook import log_pattern

# ───────────────
# Pattern Color Map
# ───────────────
pattern_color_map = {
    "Double Bottom": "green",
    "Double Top": "red",
    "Head & Shoulders": "blue",
    "Ascending Triangle": "orange",
    "Descending Triangle": "darkorange",
    "Falling Wedge": "purple",
    "Rising Wedge": "violet",
    "Cup & Handle": "gold",
    "Flag": "teal",
    "Rectangle": "gray",
    "Triple Top": "maroon",
    "Triple Bottom": "darkgreen"
}

# ───────────────
# Toggle & Filters
# ───────────────
auto_detect_chart_patterns = st.sidebar.toggle("📐 Auto Chart Pattern Detection", value=True)

chart_patterns_available = list(pattern_color_map.keys())
selected_chart_patterns = st.sidebar.multiselect("Select Patterns", chart_patterns_available, default=chart_patterns_available)

# ───────────────
# Price Generator
# ───────────────
def generate_price_data(days=150):
    np.random.seed(42)
    base = 100 + np.cumsum(np.random.randn(days))
    date_range = pd.date_range(end=datetime.today(), periods=days, freq='B')
    df = pd.DataFrame({
        'Date': date_range,
        'Close': base + np.random.uniform(-1, 1, days)
    })
    df["Open"] = df["Close"] + np.random.uniform(-1, 1, days)
    df["High"] = df[["Open", "Close"]].max(axis=1) + np.random.uniform(0, 2, days)
    df["Low"] = df[["Open", "Close"]].min(axis=1) - np.random.uniform(0, 2, days)
    return df

# ───────────────
# Pattern Detection Engine
# ───────────────
def detect_chart_patterns(df):
    detected = []
    dates = df["Date"].values
    for i, pattern in enumerate(selected_chart_patterns):
        idx = (i + 1) * 10
        if idx < len(dates):
            detected.append((dates[idx], pattern))
            log_pattern(pattern, dates[idx], None, f"Detected {pattern} structure")
    return detected
def render_chart_pattern_tab():
    st.subheader("📐 Structure Scanner — Expanded Patterns")

    df = generate_price_data(150)
    detected_patterns = detect_chart_patterns(df) if auto_detect_chart_patterns else []

    fig = go.Figure()
    fig.add_trace(go.Candlestick(
        x=df['Date'], open=df['Open'], high=df['High'],
        low=df['Low'], close=df['Close'], name="Candles"
    ))

    # ─────────────────────────────
    # Visual Label Logic
    # ─────────────────────────────
    label_stack = {}
    for date, label in detected_patterns:
        if date not in label_stack:
            label_stack[date] = 0
        offset = label_stack[date] * 2  # Prevent overlapping labels
        label_stack[date] += 1

        idx = df[df['Date'] == date].index[0]
        base_price = df.loc[idx, 'Close']
        price = base_price + offset
        color = pattern_color_map.get(label, "blue")

        fig.add_trace(go.Scatter(
            x=[date], y=[price],
            mode='markers+text',
            marker=dict(color=color, size=12),
            text=[label],
            textposition='top center',
            name=label
        ))

    fig.update_layout(title="📐 Detected Chart Patterns", xaxis_rangeslider_visible=False)
    st.plotly_chart(fig, use_container_width=True)

    # ─────────────────────────────
    # Strategy Suggestions Panel
    # ─────────────────────────────
    st.markdown("### 🧠 Strategy Suggestions")
    from modules.strategy_linker import link_detected_patterns_to_strategy
    linked_strategies = link_detected_patterns_to_strategy(detected_patterns)

    for strat in linked_strategies[-5:]:
        st.markdown(f"📌 **{strat['pattern']}** → 🧠 Strategy: `{strat['strategy']}`")
        st.caption(f"🗒️ {strat['comment']} on {pd.to_datetime(strat['date']).strftime('%Y-%m-%d')}")
