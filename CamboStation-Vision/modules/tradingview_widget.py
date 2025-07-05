import streamlit as st

def render_tradingview_widget():
    st.subheader("🌐 TradingView Widget — Live Chart Panel")

    selected_symbol = st.selectbox("📈 Select Symbol", ["NASDAQ:AAPL", "NASDAQ:TSLA", "NYSE:MSFT", "SPY", "BTCUSD", "ETHUSD"])

    selected_interval = st.selectbox("⏱️ Select Timeframe", ["1", "5", "15", "30", "60", "D", "W", "M"])

    selected_theme = st.radio("🎨 Theme", ["Dark", "Light"])

    theme_str = "dark" if selected_theme == "Dark" else "light"

    widget_url = f"https://s.tradingview.com/embed-widget/advanced-chart/?symbol={selected_symbol}&interval={selected_interval}&theme={theme_str}"

    st.markdown(f"""
        <iframe 
            src="{widget_url}" 
            width="100%" 
            height="600" 
            frameborder="0" 
            allowtransparency="true" 
            scrolling="no">
        </iframe>
    """, unsafe_allow_html=True)

    st.caption("🧠 TradingView widget embedded — fully interactive and live.")
