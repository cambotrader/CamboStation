import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objs as go
from datetime import datetime

# Generate price + volume data
def generate_chart_data(days=150):
    np.random.seed(42)
    base = 100 + np.cumsum(np.random.randn(days))
    date_range = pd.date_range(end=datetime.today(), periods=days, freq='B')
    df = pd.DataFrame({
        'Date': date_range,
        'Open': base + np.random.uniform(-1, 1, days),
        'High': base + np.random.uniform(0, 2, days),
        'Low': base - np.random.uniform(0, 2, days),
        'Close': base + np.random.uniform(-1, 1, days),
        'Volume': np.random.randint(500000, 5000000, days)
    })
    return df

# Render the chart tab
def render_chart_tab():
    st.subheader("📈 Price Chart Overview")

    df = generate_chart_data()

    fig = go.Figure()
    fig.add_trace(go.Candlestick(
        x=df['Date'],
        open=df['Open'], high=df['High'],
        low=df['Low'], close=df['Close'],
        name="Candles"
    ))

    fig.add_trace(go.Bar(
        x=df['Date'], y=df['Volume'],
        marker_color='lightblue',
        name="Volume",
        yaxis='y2'
    ))

    fig.update_layout(
        title="📊 Price Action + Volume",
        xaxis_rangeslider_visible=False,
        yaxis=dict(title='Price'),
        yaxis2=dict(title='Volume', overlaying='y', side='right', showgrid=False)
    )

    st.plotly_chart(fig, use_container_width=True)
