import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import streamlit.components.v1 as components
import requests
from datetime import datetime, timedelta
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import pandas_ta as ta

# Load FinBERT
@st.cache_resource
def load_finbert():
    tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")
    model = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert")
    return tokenizer, model

tokenizer, model = load_finbert()
LABELS = ["negative", "neutral", "positive"]
COLORS = {
    "positive": "rgba(0,200,0,0.2)",
    "neutral": "rgba(180,180,0,0.2)",
    "negative": "rgba(200,0,0,0.2)"
}

def get_sentiment(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    probs = torch.nn.functional.softmax(outputs.logits, dim=1)[0]
    return LABELS[probs.argmax()]

def fetch_headlines(ticker, api_key):
    url = f"https://newsapi.org/v2/everything?q={ticker}&language=en&sortBy=publishedAt&pageSize=5&apiKey={api_key}"
    response = requests.get(url)
    if response.status_code != 200:
        return []
    data = response.json()
    return [
        {
            "headline": article["title"],
            "date": datetime.strptime(article["publishedAt"], "%Y-%m-%dT%H:%M:%SZ")
        }
        for article in data.get("articles", []) if article.get("title") and article.get("publishedAt")
    ]

def generate_sentiment_zones(headlines):
    zones = []
    for h in headlines:
        label = get_sentiment(h["headline"])
        zones.append({
            "start": h["date"] - timedelta(days=1),
            "end": h["date"] + timedelta(days=1),
            "color": COLORS[label]
        })
    return zones

def detect_ma_signals(df):
    signals, markers = [], []
    df["MA50"] = df["Close"].rolling(50).mean()
    df["MA200"] = df["Close"].rolling(200).mean()
    df.dropna(inplace=True)

    last = df.iloc[-1]
    prev = df.iloc[-2]

    if prev["MA50"] < prev["MA200"] and last["MA50"] > last["MA200"]:
        signals.append("📈 MA50 crossover above MA200")
        markers.append({"index": df.index[-1], "label": "MA Xover", "price": last["Close"]})

    if prev["Close"] < prev["MA50"] and last["Close"] > last["MA50"]:
        signals.append("🚀 Breakout above MA50")
        markers.append({"index": df.index[-1], "label": "Breakout", "price": last["Close"]})

    return signals, markers

def plot_chart(df, ticker, signals=None, zones=None):
    fig = go.Figure()

    fig.add_trace(go.Candlestick(
        x=df.index, open=df["Open"], high=df["High"],
        low=df["Low"], close=df["Close"],
        increasing_line_color="limegreen",
        decreasing_line_color="crimson"
    ))

    fig.add_trace(go.Scatter(x=df.index, y=df["MA50"], mode="lines", name="MA50", line=dict(color="blue")))
    fig.add_trace(go.Scatter(x=df.index, y=df["MA200"], mode="lines", name="MA200", line=dict(color="orange")))

    if zones:
        for z in zones:
            fig.add_vrect(x0=z["start"], x1=z["end"], fillcolor=z["color"], opacity=0.15, line_width=0)

    if signals:
        for s in signals:
            fig.add_trace(go.Scatter(
                x=[s["index"]], y=[s["price"]],
                mode="markers+text", text=[s["label"]],
                marker=dict(symbol="star", size=12, color="gold"),
                textposition="top center", showlegend=False
            ))

    fig.update_layout(title=f"{ticker.upper()} – John AI Trading Cockpit", template="plotly_white",
                      xaxis_title="Date", yaxis_title="Price",
                      xaxis_rangeslider_visible=False)

    st.plotly_chart(fig, use_container_width=True)

# Streamlit App
st.set_page_config(page_title="John AI Trading Cockpit", layout="wide")
st.title("🧠 John AI Trading Cockpit")

ticker = st.text_input("Enter Ticker Symbol", "AAPL").upper()
if not ticker:
    st.stop()

df = yf.download(ticker, period="1y", progress=False, auto_adjust=True)
if df.empty:
    st.error("No price data.")
    st.stop()

ma_50 = df['Close'].rolling(50).mean()
ma_200 = df['Close'].rolling(200).mean()
try:
    st.write(f"📉 50-day MA: **{float(ma_50.iloc[-1]):.2f}**")
except:
    st.warning("50-day MA not available.")

try:
    st.write(f"📈 200-day MA: **{float(ma_200.iloc[-1]):.2f}**")
except:
    st.warning("200-day MA not available.")

mode = st.radio("Chart View:", ["Plotly Candlestick", "TradingView Embed", "AI Signal Chart"])

if mode == "Plotly Candlestick":
    df["MA50"] = df["Close"].rolling(50).mean()
    df["MA200"] = df["Close"].rolling(200).mean()
    plot_chart(df, ticker)

elif mode == "TradingView Embed":
    tv = f"""
    <iframe src="https://s.tradingview.com/widgetembed/?symbol={ticker}&interval=D&theme=dark&style=1"
    width="100%" height="500" frameborder="0" allowtransparency="true" scrolling="no"></iframe>
    """
    components.html(tv, height=520)

elif mode == "AI Signal Chart":
    df["MA50"] = df["Close"].rolling(50).mean()
    df["MA200"] = df["Close"].rolling(200).mean()

    news_key = "9fb37b4d807e43e3a2eaeba30d446b6d"
    headlines = fetch_headlines(ticker, news_key)
    zones = generate_sentiment_zones(headlines)

    patterns = {
        "Hammer": ta.cdlhammer,
        "Doji": ta.cdldoji,
        "Engulfing": ta.cdlengulfing,
        "Morning Star": ta.cdlmorningstar,
        "Shooting Star": ta.cdlshootingstar,
        "Hanging Man": ta.cdlhangingman,
        "Piercing Line": ta.cdlpiercing
    }

    selected = st.selectbox("🔎 Candlestick Pattern to Highlight", list(patterns.keys()))
    df["pattern"] = patterns[selected](df["Open"], df["High"], df["Low"], df["Close"])
    pattern_hits = df[df["pattern"] != 0]
    pattern_markers = [{"index": i, "label": selected, "price": df.loc[i]["Close"]} for i in pattern_hits.index]

    if st.checkbox("ℹ️ Show Pattern Description"):
        desc = {
            "Hammer": "Bullish reversal with small body + long lower wick.",
            "Doji": "Indecision pattern: open ≈ close.",
            "Engulfing": "Bullish if green body fully engulfs previous red.",
            "Morning Star": "3-bar bullish reversal: red → doji → green.",
            "Shooting Star": "Bearish reversal with long upper wick.",
            "Hanging Man": "Potential top with long lower wick after uptrend.",
            "Piercing Line": "Green closes over halfway into previous red candle."
        }
        st.info(desc[selected])

    ma_signals, ma_markers = detect_ma_signals(df)
    all_markers = pattern_markers + ma_markers

    plot_chart(df, ticker, signals=all_markers, zones=zones)

    if st.checkbox("📝 Show Summary"):
        st.success(f"""
        Pattern: **{selected}** found at **{len(pattern_markers)}** locations  
        Signals: {' / '.join(ma_signals) if ma_signals else 'None'}
        """.strip())
