import yfinance as yf

def moving_average(ticker):
    data = yf.Ticker(ticker).history(period="1y")
    if data.empty or "Close" not in data:
        return f"No data found for {ticker}"

    ma50 = data["Close"].rolling(window=50).mean().iloc[-1]
    ma200 = data["Close"].rolling(window=200).mean().iloc[-1]

    return f"{ticker.upper()} - 50-day MA: ${ma50:.2f}, 200-day MA: ${ma200:.2f}"



