import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objs as go
from datetime import datetime
from modules.pattern_logbook import log_pattern  # Optional: used for journal logging
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# 📋 Pattern definitions
candlestick_patterns = {
    "Bullish Engulfing": {"type": "bull", "color": "green"},
    "Bearish Engulfing": {"type": "bear", "color": "red"},
    "Doji": {"type": "neutral", "color": "gold"},
    "Hammer": {"type": "bull", "color": "blue"},
    "Shooting Star": {"type": "bear", "color": "purple"},
}

# 📈 Generate dummy price data
def generate_candle_data(days=150):
    np.random.seed(42)
    base = 100 + np.cumsum(np.random.randn(days))
    date_range = pd.date_range(end=datetime.today(), periods=days, freq='B')
    df = pd.DataFrame({
        'Date': date_range,
        'Open': base + np.random.uniform(-1, 1, days),
        'High': base + np.random.uniform(0, 2, days),
        'Low': base - np.random.uniform(0, 2, days),
        'Close': base + np.random.uniform(-1, 1, days)
    })
    return df

# 🔍 Detect true candlestick patterns with reversal ratings
def detect_candlestick_patterns(df):
    detected = []
    for i in range(1, len(df)):
        o, h, l, c = df.loc[i, ["Open", "High", "Low", "Close"]]
        prev_o, prev_c = df.loc[i - 1, ["Open", "Close"]]

        body = abs(c - o)
        range_ = h - l
        rating = "Weak"

        # Engulfing
        if c > o and prev_c < prev_o and c > prev_o and o < prev_c:
            rating = "Strong" if body > 1 else "Moderate"
            detected.append((df.loc[i, "Date"], "Bullish Engulfing", rating))
        elif c < o and prev_c > prev_o and c < prev_o and o > prev_c:
            rating = "Strong" if body > 1 else "Moderate"
            detected.append((df.loc[i, "Date"], "Bearish Engulfing", rating))
        # Doji
        elif body < 0.15 and range_ > 1:
            rating = "Neutral"
            detected.append((df.loc[i, "Date"], "Doji", rating))
        # Hammer
        elif body < 1 and (o - l > body * 2) and c > o:
            rating = "Moderate"
            detected.append((df.loc[i, "Date"], "Hammer", rating))
        # Shooting Star
        elif body < 1 and (h - c > body * 2) and c < o:
            rating = "Moderate"
            detected.append((df.loc[i, "Date"], "Shooting Star", rating))

    return detected

# 🎨 Render tab with chart overlay
def render_pattern_tab():
    st.subheader("📈 Candlestick Pattern Overlay Engine")

    df = generate_candle_data()
    patterns = detect_candlestick_patterns(df)

    fig = go.Figure()
    fig.add_trace(go.Candlestick(
        x=df['Date'], open=df['Open'], high=df['High'],
        low=df['Low'], close=df['Close'], name="Candles"
    ))

    label_stack = {}

    for date, label, rating in patterns:
        idx = df[df['Date'] == date].index[0]
        base_price = df.loc[idx, 'Close']

        if date not in label_stack:
            label_stack[date] = 0
        offset = label_stack[date] * 2
        label_stack[date] += 1

        price = base_price + offset
        color = candlestick_patterns[label]["color"]

        fig.add_trace(go.Scatter(
            x=[date], y=[price],
            mode="markers+text",
            marker=dict(color=color, size=10),
            text=[f"{label} ({rating})"],
            textposition="top center",
            name=label
        ))

    fig.update_layout(title="📈 Candlestick Signal Overlay", xaxis_rangeslider_visible=False)
    st.plotly_chart(fig, use_container_width=True)

    st.caption("🧠 Reversal Logic Activated • Tactical Overlay Engine Online")
