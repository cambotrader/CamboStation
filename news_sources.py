# news_sources.py

import streamlit as st
import feedparser
import socket

# Set a timeout for all feed requests (in seconds)
socket.setdefaulttimeout(5)

# List of RSS feeds
rss_feeds = [
    "https://www.cnbc.com/id/100003114/device/rss/rss.html",
    "https://feeds.finance.yahoo.com/rss/2.0/headline?s=AAPL&region=US&lang=en-US",
    "https://www.investing.com/rss/news_285.rss",
    "https://www.bloomberg.com/feed/podcast/etf-report.xml"
]

def fetch_rss(rss_feeds):
    items = []
    for url in rss_feeds:
        try:
            parsed = feedparser.parse(url)
            items.extend(parsed.entries[:5])
        except Exception as e:
            st.warning(f"⚠️ Couldn't fetch RSS from {url}: {e}")
    return items

def show_combined_news(ticker):
    st.subheader("📰 News Headlines + Sentiment")
    rss_items = fetch_rss(rss_feeds)

    if not rss_items:
        st.info("No news headlines could be loaded at this time.")
        return

    for entry in rss_items:
        title = entry.get("title", "No title")
        link = entry.get("link", "")
        st.write(f"🔹 [{title}]({link})")
