import pandas as pd
import plotly.graph_objects as go
from ta.trend import SMAIndicator, MACD
from ta.momentum import RSIIndicator

def generate_chart(df):
    # Moving Averages
    ma50 = SMAIndicator(close=df['close'], window=50)
    ma200 = SMAIndicator(close=df['close'], window=200)
    df['MA50'] = ma50.sma_indicator()
    df['MA200'] = ma200.sma_indicator()

    # RSI
    rsi = RSIIndicator(close=df['close'], window=14)
    df['RSI'] = rsi.rsi()

    # MACD
    macd_obj = MACD(close=df['close'])
    df['macd'] = macd_obj.macd()
    df['macd_signal'] = macd_obj.macd_signal()
    df['macd_hist'] = macd_obj.macd_diff()

    # Chart
    fig = go.Figure(data=[go.Candlestick(
        x=df['date'],
        open=df['open'],
        high=df['high'],
        low=df['low'],
        close=df['close'],
        name='Price'
    )])

    fig.add_trace(go.Scatter(x=df['date'], y=df['MA50'], line=dict(color='blue'), name='MA50'))
    fig.add_trace(go.Scatter(x=df['date'], y=df['MA200'], line=dict(color='red'), name='MA200'))

    fig.update_layout(title='CamboStation Tactical Chart', xaxis_rangeslider_visible=False)

    return fig
