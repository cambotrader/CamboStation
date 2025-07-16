import streamlit as st
from regime_console_core import load_sample_ohlc
import talib

st.title("📈 Candlestick Pattern Recognition")
df = load_sample_ohlc()
hammer = talib.CDLHAMMER(df.Open, df.High, df.Low, df.Close)
df["Hammer"] = hammer
st.dataframe(df[["Open", "High", "Low", "Close", "Hammer"]].tail(10))
