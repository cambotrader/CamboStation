# streamlit_app.py

from chart_module import plot_price_chart
from signal_engine import detect_ai_patterns
import streamlit as st
import streamlit.components.v1 as components
import yfinance as yf

st.set_page_config(page_title="Trading Hub", layout="wide")
st.title("🚀 Cambo Trading Cockpit")

ticker = st.text_input("Enter Ticker Symbol", placeholder="e.g. AAPL, TSLA").upper()

if ticker:
    df = yf.download(ticker, period="1y", progress=False, auto_adjust=True)
    if df.empty or "Close" not in df.columns:
        st.error(f"No data for {ticker}")
        st.stop()

    st.header("📊 Technical Indicators")
    close = df["Close"]
    ma50 = float(close.rolling(50).mean().iloc[-1])
    ma200 = float(close.rolling(200).mean().iloc[-1])
    st.write(f"• 50-day MA: **{ma50:.2f}**")
    st.write(f"• 200-day MA: **{ma200:.2f}**")

    st.header("📈 Price Chart View")
    chart_mode = st.radio("Choose chart type:", ("Plotly Candlestick", "TradingView Embed", "AI Signal Chart"))

    if chart_mode == "Plotly Candlestick":
        show_ma50 = st.checkbox("Include MA50", value=True)
        show_ma200 = st.checkbox("Include MA200", value=True)
        plot_price_chart(ticker, show_ma50, show_ma200)

    elif chart_mode == "TradingView Embed":
        tv_embed = f"""
        <iframe src="https://s.tradingview.com/widgetembed/?symbol={ticker}&interval=D&theme=dark&style=1&toolbar_bg=000000&locale=en"
                width="100%" height="500" frameborder="0" allowtransparency="true" scrolling="no" title="TradingView">
        </iframe>
        """
        components.html(tv_embed, height=520)

    elif chart_mode == "AI Signal Chart":
        st.subheader("🧠 AI Pattern Detection")
        df_ai = yf.download(ticker, period="6mo", progress=False, auto_adjust=True)
        if df_ai.empty:
            st.error("No AI data found.")
            st.stop()

        signals, markers, zones, summary = detect_ai_patterns(df_ai, ticker)

        st.success("🚀 Signals Detected:")
        for sig in signals:
            st.markdown(f"- {sig}")

        st.markdown("📍 Signals are shown on the chart below")
        plot_price_chart(ticker, show_ma50=True, show_ma200=True, signals=markers, sentiment=zones)

        if st.checkbox("📝 Show AI-Generated Summary"):
            st.info(summary)
