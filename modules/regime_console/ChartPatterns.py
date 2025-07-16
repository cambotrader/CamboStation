import streamlit as st
from regime_console_core import load_sample_ohlc

try:
    from patternpy.tradingpatterns import head_and_shoulders
    st.title("🗺️ PatternPy Chart Recognition")
    df = load_sample_ohlc()
    df = head_and_shoulders(df)
    st.dataframe(df.tail(10))
except ImportError:
    st.warning("PatternPy not installed. Clone from GitHub to enable chart pattern detection.")
