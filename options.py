# streamlit_app.py

import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px
from typing import Tuple, Optional

st.set_page_config(page_title="Trading Hub Dashboard", layout="wide")
st.title("?? Trading Hub Dashboard")

# -- Helper Functions --

def moving_average(ticker: str, w1: int = 50, w2: int = 200) -> Tuple[float, float]:
    """Return latest 50- and 200-day moving averages."""
    data = yf.download(ticker, period="1y", progress=False)["Close"]
    return data.rolling(w1).mean().iloc[-1], data.rolling(w2).mean().iloc[-1]

def detect_patterns(ticker: str) -> str:
    """Mock chart-pattern detector (replace with TA logic!)."""
    return f"Detected chart patterns for {ticker.upper()} – mock output"

def fetch_option_chain(
    ticker: str, expiry: str
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Fetch calls & puts DataFrames for the given ticker & expiry.
    Returns (calls_df, puts_df).
    """
    tk = yf.Ticker(ticker)
    try:
        chain = tk.option_chain(expiry)
        calls = chain.calls.copy()[["strike", "lastPrice", "impliedVolatility"]]
        puts  = chain.puts.copy()[["strike", "lastPrice", "impliedVolatility"]]
        return calls, puts
    except Exception as e:
        st.error(f"Error fetching options for {ticker}@{expiry}: {e}")
        return pd.DataFrame(), pd.DataFrame()

def fetch_news_sentiment(ticker: str) -> str:
    """Stub: return the latest 5 headlines for the ticker."""
    stock = yf.Ticker(ticker)
    news = getattr(stock, "news", []) or []
    if not news:
        return f"No news found for {ticker.upper()}."
    titles = [item.get("title","No title") for item in news[:5]]
    return "\n\n".join(titles)

# -- App Layout --

# 1) Ticker Input
ticker = st.text_input("Enter Ticker Symbol", placeholder="e.g. AAPL, TSLA").upper()

if ticker:
    # 2) Technical Indicators
    st.header("?? Technical Indicators")
    try:
        ma50, ma200 = moving_average(ticker)
        st.write(f"• 50-day MA: **{ma50:.2f}**\n• 200-day MA: **{ma200:.2f}**")
    except Exception as e:
        st.error(f"Error fetching MAs for {ticker}: {e}")

    # 3) Chart Patterns
    st.header("?? Chart Patterns")
    st.write(detect_patterns(ticker))

    # 4) Options Chain w/ Expiry Dropdown
    st.header("?? Options Chain")
    tk = yf.Ticker(ticker)
    expiries = tk.options or []
    if expiries:
        selected = st.selectbox("Choose Expiry", expiries)
        calls_df, puts_df = fetch_option_chain(ticker, selected)

        if not calls_df.empty and not puts_df.empty:
            st.subheader(f"{ticker} (Exp: {selected})")

            st.markdown("**Calls**")
            st.table(calls_df.style.format({
                "lastPrice": "${:.2f}",
                "impliedVolatility": "{:.2%}"
            }))

            st.markdown("**Puts**")
            st.table(puts_df.style.format({
                "lastPrice": "${:.2f}",
                "impliedVolatility": "{:.2%}"
            }))

            # IV-Skew Bar Charts
            fig_c = px.bar(
                calls_df, x="strike", y="impliedVolatility",
                labels={"impliedVolatility":"IV"}, title="Calls IV by Strike"
            )
            st.plotly_chart(fig_c, use_container_width=True)

            fig_p = px.bar(
                puts_df, x="strike", y="impliedVolatility",
                labels={"impliedVolatility":"IV"}, title="Puts IV by Strike"
            )
            st.plotly_chart(fig_p, use_container_width=True)
        else:
            st.warning("No options data available for this expiry.")
    else:
        st.warning(f"No expiries found for {ticker}.")

    # 5) News Sentiment (Headlines Stub)
    st.header("?? News Sentiment")
    st.write(fetch_news_sentiment(ticker))

