import streamlit as st

def show_education_tab():
    st.title("🎓 CamboStation™ Academy")
    st.markdown("Level up your trading skills with pattern recognition, indicators, asset breakdowns, and tactical strategies.")

    # --- Candlestick Patterns ---
    with st.expander("🕯️ Candlestick Patterns"):
        st.subheader("Single-Bar Patterns")
        st.markdown("- **Doji**: Market indecision, possible reversal.\n- **Hammer/Inverted Hammer**: Bullish reversal after a downtrend.\n- **Shooting Star**: Bearish reversal at the top.")

        st.subheader("Two-Bar Patterns")
        st.markdown("- **Bullish/Bearish Engulfing**: Strong reversal confirmation.\n- **Harami**: Trend stall or reversal signal.\n- **Tweezer Top/Bottom**: Double rejection signal.")

        st.subheader("Three-Bar Patterns")
        st.markdown("- **Morning Star / Evening Star**: Reversal with confirmation.\n- **Three White Soldiers / Black Crows**: Strong continuation patterns.")

    # --- Chart Patterns ---
    with st.expander("📈 Chart Patterns"):
        st.subheader("Reversal Patterns")
        st.markdown("- **Head and Shoulders**\n- **Double Top / Bottom**\n- **Rising / Falling Wedges**")

        st.subheader("Continuation Patterns")
        st.markdown("- **Bullish / Bearish Flags**\n- **Symmetrical / Ascending / Descending Triangles**\n- **Cup and Handle**")

        st.subheader("Advanced Patterns")
        st.markdown("- **Harmonic Setups (Gartley, Butterfly, Crab, Bat)**\n- **Broadening Wedges**\n- **Wyckoff Accumulation / Distribution**")

    # --- Indicators & Oscillators ---
    with st.expander("📊 Indicators & Oscillators"):
        st.markdown("- **RSI**: Overbought/Oversold momentum index.\n- **MACD**: Trend-following momentum indicator.\n- **Stochastic Oscillator**: Price momentum in comparison to highs/lows.\n- **VWAP**: Average price traded based on volume.\n- **Bollinger Bands**: Volatility and mean-reversion boundaries.")

    # --- Asset Class Playbooks ---
    with st.expander("📂 Market Playbooks"):
        st.subheader("🧮 Stocks")
        st.markdown("Day, swing, and long-term trading methods. Sector rotation and breakout setups.")

        st.subheader("💹 Forex")
        st.markdown("Pip structure, majors/crosses, global macro plays, central bank impacts.")

        st.subheader("🧠 Options")
        st.markdown("Greeks, multi-leg strategies (spreads, condors), earnings plays, volatility trading.")

        st.subheader("🔄 Futures")
        st.markdown("Margin structure, expiration cycles, hedging tools.")

        st.subheader("₿ Crypto")
        st.markdown("Wallet security, exchange liquidity, tokenomics, staking basics.")

        st.subheader("💵 Bonds & T-Bills")
        st.markdown("Yield curve understanding, interest rate impact, laddering strategies.")

    # --- Strategy Breakdown ---
    with st.expander("🧠 Strategy Vault"):
        st.subheader("Beginner")
        st.markdown("- **Dollar-cost averaging (DCA)**\n- **Simple moving average crossovers**\n- **Trailing stop use**")

        st.subheader("Intermediate")
        st.markdown("- **Breakout retest entries**\n- **Relative strength sector picking**\n- **Swing setups based on chart structure**")

        st.subheader("Advanced")
        st.markdown("- **Multi-leg option spreads**\n- **Macroeconomic sentiment rotation**\n- **Quantified backtesting**")

    # --- Risk Management Essentials ---
    with st.expander("🧯 Risk Management"):
        st.markdown("- **Max loss per trade / day rules**\n- **Risk/reward profiling (e.g., 3:1 setups)**\n- **Diversification and correlation exposure**\n- **Psychological resilience (journaling, review loops)**")
