import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objs as go
from datetime import datetime

# ──────────────────────────────────────────────────────
# Simulated data generator (placeholder for live APIs)
# ──────────────────────────────────────────────────────
def generate_price_data(days=100, ticker="AAPL"):
    np.random.seed(len(ticker))
    price = 100 + np.cumsum(np.random.randn(days))
    date_range = pd.date_range(end=datetime.today(), periods=days, freq='B')
    df = pd.DataFrame({
        'Date': date_range,
        'Open': price + np.random.uniform(-1, 1, days),
        'High': price + np.random.uniform(0, 2, days),
        'Low': price - np.random.uniform(0, 2, days),
        'Close': price + np.random.uniform(-1, 1, days),
        'Volume': np.random.randint(1000000, 5000000, days)
    })
    return df

# ──────────────────────────────────────────────────────
# Indicator overlays
# ──────────────────────────────────────────────────────
def add_indicators(df, indicators):
    if "SMA" in indicators:
        df['SMA_20'] = df['Close'].rolling(window=20).mean()
    if "EMA" in indicators:
        df['EMA_20'] = df['Close'].ewm(span=20).mean()
    if "RSI" in indicators:
        delta = df['Close'].diff()
        gain = delta.clip(lower=0)
        loss = -1 * delta.clip(upper=0)
        avg_gain = gain.rolling(window=14).mean()
        avg_loss = loss.rolling(window=14).mean()
        rs = avg_gain / avg_loss
        df['RSI'] = 100 - (100 / (1 + rs))
    if "Bollinger" in indicators:
        df['BB_MID'] = df['Close'].rolling(window=20).mean()
        df['BB_STD'] = df['Close'].rolling(window=20).std()
        df['BB_UPPER'] = df['BB_MID'] + 2 * df['BB_STD']
        df['BB_LOWER'] = df['BB_MID'] - 2 * df['BB_STD']
    if "VWAP" in indicators:
        df['VWAP'] = (df['Close'] * df['Volume']).cumsum() / df['Volume'].cumsum()
    return df

# ──────────────────────────────────────────────────────
# Chart builder with platform style logic
# ──────────────────────────────────────────────────────
def render_chart(df, style, indicators):
    fig = go.Figure()

    if style in ["TradingView", "ThinkOrSwim", "TC2000", "TrendSpider"]:
        fig.add_trace(go.Candlestick(
            x=df['Date'],
            open=df['Open'], high=df['High'],
            low=df['Low'], close=df['Close'],
            name="Candles"))
    elif style == "Line":
        fig.add_trace(go.Scatter(
            x=df['Date'], y=df['Close'],
            mode='lines', name='Line Price', line=dict(color='blue')))
    else:
        fig.add_trace(go.Bar(
            x=df['Date'], y=df['Close'], name="Close Price"))

    if "SMA" in indicators and 'SMA_20' in df:
        fig.add_trace(go.Scatter(x=df['Date'], y=df['SMA_20'], name="SMA 20", line=dict(color="green")))
    if "EMA" in indicators and 'EMA_20' in df:
        fig.add_trace(go.Scatter(x=df['Date'], y=df['EMA_20'], name="EMA 20", line=dict(color="red")))
    if "RSI" in indicators and 'RSI' in df:
        fig.add_trace(go.Scatter(x=df['Date'], y=df['RSI'], name="RSI", line=dict(color="purple")))
    if "Bollinger" in indicators:
        fig.add_trace(go.Scatter(x=df['Date'], y=df['BB_UPPER'], name="BB Upper", line=dict(color="orange")))
        fig.add_trace(go.Scatter(x=df['Date'], y=df['BB_LOWER'], name="BB Lower", line=dict(color="orange", dash="dot")))
    if "VWAP" in indicators and 'VWAP' in df:
        fig.add_trace(go.Scatter(x=df['Date'], y=df['VWAP'], name="VWAP", line=dict(color="gray")))

    fig.update_layout(title=f"🧠 {style} Style Chart", xaxis_rangeslider_visible=False)
    return fig

# ──────────────────────────────────────────────────────
# Main Panel
# ──────────────────────────────────────────────────────
def render_chart_tab():
    st.subheader("📈 Tactical Chart Panel — TradingView Default")
    col1, col2, col3 = st.columns(3)

    with col1:
        ticker = st.text_input("Ticker", value="AAPL")
    with col2:
        style = st.selectbox("Chart Style", ["TradingView", "TrendSpider", "ThinkOrSwim", "TC2000", "Line", "Bar"])
    with col3:
        timeframe = st.selectbox("Timeframe (Simulated)", ["1D", "1H", "30min", "15min"])

    st.markdown("---")
    indicators = st.multiselect("🧩 Select Indicators to Overlay", ["SMA", "EMA", "RSI", "Bollinger", "VWAP"])
    df = generate_price_data(days=150, ticker=ticker)
    df = add_indicators(df, indicators)

    chart = render_chart(df, style, indicators)
    st.plotly_chart(chart, use_container_width=True)

    st.markdown("---")
    st.caption("🧠 CamboStation™ Chart Engine — Powered by Sniper Mode Logic")

