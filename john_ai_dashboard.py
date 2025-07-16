import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

from candles_engine import detect_patterns
from candlestick_definitions import candlestick_definitions
from chart_patterns_engine import detect_chart_patterns
from chart_patterns_definitions import chart_patterns
from chart_provider_definitions import chart_providers
from chart_embed_logic import get_chart_embed, is_native_chart, provider_supports_overlay

st.set_page_config(page_title="John AI Global Dashboard", layout="wide")
st.title("🧠 John AI | Global Market Cockpit")

# === Inputs
symbol = st.sidebar.text_input("📈 Symbol", "AAPL").upper()
interval = st.sidebar.selectbox("⏱️ Interval", ["1m", "5m", "15m", "1h", "1d"], index=4)
period = st.sidebar.selectbox("📅 Lookback", ["5d", "1mo", "3mo", "6mo", "1y"], index=1)

provider_names = [p["name"] for p in chart_providers]
chart_source = st.sidebar.selectbox("📊 Chart Provider", provider_names, index=0)

# === Group Pattern Definitions
def group_defs(defs):
    grouped = {}
    for p in defs:
        grouped.setdefault(p["group"], []).append(p)
    return grouped

# === Candlestick Controls
candle_settings = {}
st.sidebar.markdown("## 🕯️ Candlestick Patterns")
for group, patterns in group_defs(candlestick_definitions).items():
    with st.sidebar.expander(f"📂 {group}", expanded=False):
        for p in patterns:
            enabled = st.checkbox(f"{p['emoji']} {p['name']}", value=False)
            show = st.checkbox(f"📊 Show on Chart – {p['name']}", value=False)
            st.caption(f"📘 {p['description']}\n🎯 {p['trigger']}")
            candle_settings[p["name"]] = {"enabled": enabled, "show_on_chart": show, "emoji": p["emoji"]}

# === Chart Pattern Controls
chart_settings = {}
st.sidebar.markdown("## 📐 Chart Patterns")
for group, patterns in group_defs(chart_patterns).items():
    with st.sidebar.expander(f"📂 {group}", expanded=False):
        for p in patterns:
            enabled = st.checkbox(f"{p['emoji']} {p['name']}", value=False)
            show = st.checkbox(f"📊 Show on Chart – {p['name']}", value=False)
            st.caption(f"📘 {p['description']}\n🎯 {p['trigger']}")
            chart_settings[p["name"]] = {"enabled": enabled, "show_on_chart": show, "emoji": p["emoji"]}

# === Load Data
try:
    df = yf.download(symbol, period=period, interval=interval)
    df.dropna(inplace=True)
    df.index = pd.to_datetime(df.index)
    st.success(f"✅ Loaded {len(df)} bars for {symbol} | Interval: {interval}")

    # Pattern Detection
    candle_hits = detect_patterns(df, candle_settings)
    chart_hits = detect_chart_patterns(df, chart_settings)
    all_hits = candle_hits + chart_hits

    native_chart = is_native_chart(chart_source)
    overlay_enabled = provider_supports_overlay(chart_source)

    # === Render Plotly Chart with Overlays
    if chart_source == "Plotly":
        fig = go.Figure(data=[go.Candlestick(
            x=df.index, open=df["Open"], high=df["High"],
            low=df["Low"], close=df["Close"]
        )])

        for hit in all_hits:
            name = hit["pattern"]
            idx = hit["index"]
            emoji = hit["emoji"]
            if (
                candle_settings.get(name, {}).get("show_on_chart") or
                chart_settings.get(name, {}).get("show_on_chart")
            ):
                fig.add_annotation(
                    x=df.index[idx],
                    y=df["High"].iloc[idx],
                    text=emoji,
                    showarrow=True,
                    arrowhead=1,
                    bgcolor="orange",
                    font=dict(size=10)
                )

        fig.update_layout(xaxis_rangeslider_visible=False, height=600)
        st.plotly_chart(fig, use_container_width=True)

    # === Embed External Chart
    else:
        embed_code = get_chart_embed(symbol, chart_source)
        if not embed_code:
            st.warning(f"⚠️ {chart_source} does not support symbol: {symbol}")
        else:
            st.components.v1.html(embed_code, height=600)

        if not overlay_enabled and any([
            v.get("show_on_chart") for v in candle_settings.values()
        ] + [v.get("show_on_chart") for v in chart_settings.values()]):
            st.warning(f"⚠️ '{chart_source}' does not support overlay markers. Switch to 'Plotly' or 'TradingView' to see emoji annotations.")

    # === Summary Table
    if all_hits:
        st.markdown("### 📋 Pattern Hits Summary")
        df_hits = pd.DataFrame([
            {"Time": df.index[h["index"]], "Pattern": h["pattern"], "Emoji": h["emoji"]}
            for h in all_hits
        ])
        st.dataframe(df_hits, use_container_width=True)
    else:
        st.info("No patterns detected for selected inputs.")

except Exception as e:
    st.error("🚨 Error loading data or detecting patterns.")
    st.exception(e)
