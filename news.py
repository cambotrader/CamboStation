import yfinance as yf

def fetch_news_sentiment(ticker: str) -> str:
    """
    Fetches up to 5 latest news headlines for the given ticker.
    """
    try:
        stock = yf.Ticker(ticker)
        news_items = stock.news
        if not news_items:
            return f"No news found for {ticker.upper()}."

        # Grab the first 5 headlines
        headlines = [item.get("title", "No title") for item in news_items[:5]]
        return "\n\n".join(headlines)
    except Exception as e:
        return f"Error fetching news for {ticker.upper()}: {e}"


