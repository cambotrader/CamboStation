# news_feeds.py
import requests
from textblob import TextBlob
import streamlit as st
from config import NEWS_API_KEY

def analyze_sentiment(headline):
    polarity = TextBlob(headline).sentiment.polarity
    if polarity > 0.1:
        return "🟢 Positive"
    elif polarity < -0.1:
        return "🔴 Negative"
    else:
        return "🟡 Neutral"

def fetch_newsapi_headlines(ticker):
    url = f"https://newsapi.org/v2/everything?q={ticker}&language=en&sortBy=publishedAt&pageSize=10&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    data = response.json()

    if data.get("status") != "ok":
        st.error("Failed to load news headlines.")
        return

    articles = data.get("articles", [])
    for article in articles:
        title = article["title"]
        url = article["url"]
        score = analyze_sentiment(title)
        st.markdown(f"{score} — [{title}]({url})")

def display_news(ticker):
    st.subheader("📰 News Headlines + Sentiment")
    if st.checkbox("Enable NewsAPI headlines"):
        fetch_newsapi_headlines(ticker)

import requests
from textblob import TextBlob
import streamlit as st
from config import NEWS_API_KEY

def analyze_sentiment(headline):
    polarity = TextBlob(headline).sentiment.polarity
    if polarity > 0.1:
        return "🟢 Positive"
    elif polarity < -0.1:
        return "🔴 Negative"
    else:
        return "🟡 Neutral"

def fetch_newsapi_headlines(ticker):
    url = f"https://newsapi.org/v2/everything?q={ticker}&language=en&sortBy=publishedAt&pageSize=10&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    data = response.json()

    if data.get("status") != "ok":
        st.error("Failed to load news headlines.")
        return

    articles = data.get("articles", [])
    for article in articles:
        title = article["title"]
        url = article["url"]
        score = analyze_sentiment(title)
        st.markdown(f"{score} — [{title}]({url})")

def display_news(ticker):
    st.subheader("📰 News Headlines + Sentiment")
    if st.checkbox("Enable NewsAPI headlines"):
        fetch_newsapi_headlines(ticker)
