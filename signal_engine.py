# dashboard.py
import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import requests
from datetime import datetime, timedelta
import streamlit.components.v1 as components
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# ─── Load FinBERT for Sentiment ─────────────────────────────────────────────
@st.cache_resource
def load_finbert():
    tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")
    model = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert")
    return tokenizer, model

tokenizer, model = load_finbert()
labels = ["negative", "neutral", "positive"]

def finbert_sentiment_score(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    scores = torch.nn.functional.softmax(outputs.logits, dim=1)[0]
    return labels[scores.argmax()]

# ─── Fetch Headlines (simulated for now) ────────────────────────────────────
def get_recent_headlines(ticker):
    return [
        {"date": datetime.now() - timedelta(days=1), "headline": f"{ticker.upper()} Q2 earnings beat expectations"},
        {"date": datetime.now() - timedelta(days=4), "headline": f"{ticker.upper()} under investigation for insider trading"},
        {"date": datetime.now() - timedelta(days=9), "headline": f"{ticker.upper()} signs new AI partnership deal"},
        {"date": datetime.now() - timedelta(days=13), "headline": f"{ticker.upper()} price target lowered by major bank"}
    ]

def get_sentiment_zones(headlines):
    zones = []
    color_map = {
        "positive": "rgba(0,200,0,0.2)",
        "neutral": "rgba(180,180,0,0.2)",
        "negative": "rgba(200,0,0,0.2)"
    }
    for item in headlines:
        tone = finbert_sentiment_score(item["headline"])
        zones.append({
            "start": item["date"] - timedelta(days=1),
            "end": item["date"] + timedelta(days=1),
            "color": color_map[tone],
            "label": tone
        })
    return zones

# ─── Signal Engine ──────────────────────────────────────────────────────────
def detect_signals(df):
    df["MA50"] = df["Close"].rolling(50).mean()
    df["MA200"] = df["Close"].rolling(200).mean()
    df.dropna(inplace=True)

    last = df.iloc[-1]
    prev = df.iloc[-2]

    signals = []
    markers = []

    if (prev["MA50"] < prev["MA200"]) and (last["MA50"] > last["MA200"]):
        signals.append("📈 MA50 crossed above MA200 – Bullish crossover")
        markers.append({"index": df.index[-1], "price": last["Close"], "label": "MA Crossover"})

    if (prev["Close"] < prev["MA50"]) and (last["Close"] > last["MA50"]):
        signals.append("🚀 Price broke above MA50 – Possible breakout")
        markers.append({"index": df.index[-1], "price": last["Close"], "label": "Breakout"})

    return signals, markers

# ─── Chart Function ─────────────────────────────────────────────────────────
def plot_chart(df, ticker, show_ma50=True, show_ma200=True, markers=None, zones=None):
    fig = go.Figure()

    fig.add_trace(go.Candlestick(
        x=df.index,
        open=df["Open"], high=df["High"],
        low=df["Low"], close=df["Close"],
        name="Candlesticks",
        increasing_line_color="limegreen",
        decreasing_line_color="crimson"
    ))

    if show_ma50:
        fig.add_trace(go.Scatter(
            x=df.index, y=df["MA50"],
            mode="lines", name="MA50",
            line=dict(color="blue", width=2)
        ))

    if show_ma200:
        fig.add_trace(go.Scatter(
            x=df.index, y=df["MA200"],
            mode="lines", name="MA200",
            line=dict(color="orange", width=2)
        ))

    if zones:
        for zone in zones:
            fig.add_vrect(
                x0=zone["start"], x1=zone["end"],
                fillcolor=zone["color"],
                opacity=0.15, line_width=0
            )

    if markers:
        for mark in markers:
            fig.add_trace(go.Scatter(
                x=[mark["index"]], y=[mark["price"]],
                mode="markers+text",
                marker=dict(symbol="star", size=12, color="gold"),
                text=[mark["label"]],
                textposition="top center",
                showlegend=False
            ))

    fig.update_layout(
        title=f"{ticker.upper()} Chart with Signals",
        xaxis_title="Date", yaxis_title="Price",
        xaxis_rangeslider_visible=False,
        template="plotly_white"
    )

    st.plotly_chart(fig, use_container_width=True)

# ─── Streamlit App Layout ───────────────────────────────────────────────────
st.title("🧠 Cambo AI Trading Dashboard")

ticker = st.text_input("Enter Ticker Symbol", "AAPL").upper()
if not ticker:
    st.stop()

df = yf.download(ticker, period="1y", progress=False, auto_adjust=True)
if df.empty or "Close" not in df.columns:
    st.error("No price data available.")
    st.stop()

st.write(f"• 50-day MA: **{df['Close'].rolling(50).mean().iloc[-1]:.2f}**")
st.write(f"• 200-day MA: **{df['Close'].rolling(200).mean().iloc[-1]:.2f}**")

chart_type = st.radio("Select chart view:", ["Plotly Candlestick", "TradingView Embed", "AI Signal Chart"])

if chart_type == "Plotly Candlestick":
    show_ma50 = st.checkbox("Show MA50", value=True)
    show_ma200 = st.checkbox("Show MA200", value=True)
    df["MA50"] = df["Close"].rolling(50).mean()
    df["MA200"] = df["Close"].rolling(200).mean()
    plot_chart(df, ticker, show_ma50, show_ma200)

elif chart_type == "TradingView Embed":
    tv_embed = f"""
    <iframe src="https://s.tradingview.com/widgetembed/?symbol={ticker}&interval=D&theme=dark&style=1"
            width="100%" height="500" frameborder="0" allowtransparency="true" scrolling="no">
    </iframe>
    """
    components.html(tv_embed, height=520)

elif chart_type == "AI Signal Chart":
    st.subheader("AI Pattern Detection + FinBERT Sentiment")
    signals, markers = detect_signals(df)
    headlines = get_recent_headlines(ticker)
    sentiment_zones = get_sentiment_zones(headlines)
    df["MA50"] = df["Close"].rolling(50).mean()
    df["MA200"] = df["Close"].rolling(200).mean()
    plot_chart(df, ticker, True, True, markers, sentiment_zones)

    if signals:
        st.success("📊 Signals Detected:")
        for s in signals:
            st.markdown(f"- {s}")
    else:
        st.warning("No major signals detected.")

    if st.checkbox("📝 Show AI Summary"):
        st.info(f"""
        For {ticker.upper()}, we observed:
        • {signals[0] if len(signals) > 0 else "No crossover signal"}
        • {signals[1] if len(signals) > 1 else "No breakout signal"}
        Recent news sentiment zones suggest momentum alignment with signal zones.
        """)
