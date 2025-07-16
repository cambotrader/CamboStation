import streamlit as st
import pandas as pd
import plotly.graph_objects as go

def render_candlestick_chart(asset):
    st.subheader(f"📈 Candlestick Chart: {asset.upper()}")

    # Sample synthetic OHLC data
    df = pd.DataFrame({
        "Date": pd.date_range(end=pd.Timestamp.today(), periods=30),
        "Open": pd.Series([100 + i + (i%5)*2 for i in range(30)]),
        "High": pd.Series([105 + i + (i%3)*2 for i in range(30)]),
        "Low": pd.Series([95 + i - (i%4)*2 for i in range(30)]),
        "Close": pd.Series([98 + i + (i%6)*2 for i in range(30)])
    })

    fig = go.Figure(data=[go.Candlestick(
        x=df["Date"],
        open=df["Open"],
        high=df["High"],
        low=df["Low"],
        close=df["Close"]
    )])

    fig.update_layout(xaxis_rangeslider_visible=False)
    st.plotly_chart(fig, use_container_width=True)
