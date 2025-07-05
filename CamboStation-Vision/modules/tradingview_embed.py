import streamlit as st

def render_tradingview_tab():
    st.subheader("🌐 TradingView Integration")

    # 🔲 Embedded Widget (Functional chart, no login required)
    st.markdown("""
        <iframe 
            src="https://s.tradingview.com/embed-widget/advanced-chart/?symbol=NASDAQ:AAPL&interval=D&theme=dark"
            width="100%" 
            height="600" 
            frameborder="0" 
            allowtransparency="true" 
            scrolling="no">
        </iframe>
    """, unsafe_allow_html=True)

    # 🔗 Launch Full Workspace (for login & broker tools)
    st.markdown("---")
    st.markdown("### 🔗 Open Full TradingView Workspace")
    st.markdown("[Click here to launch TradingView with full login access](https://www.tradingview.com/chart/)")
    
    # 🔌 Placeholder for other platforms
    st.markdown("---")
    st.markdown("### 📡 Other Charting Platforms")
    st.markdown("[TrendSpider](https://www.trendspider.com/) | [ThinkOrSwim](https://www.tdameritrade.com/tools-and-platforms/thinkorswim.html) | [TC2000](https://www.tc2000.com/) | [NinjaTrader](https://ninjatrader.com/) | [MT4](https://www.metatrader4.com/en/download) | [MT5](https://www.metatrader5.com/en/download)")

    st.caption("🧠 CamboStation™ cockpit module — streaming tactical platforms with redirect access.")
