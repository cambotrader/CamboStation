import streamlit as st

def render_education_tab():
    st.subheader("📚 CamboStation™ Education Center")

    sections = {
        "💡 What is a Candlestick?": "Candlesticks show the open, high, low, and close prices for an asset over a specific time.",
        "📏 RSI Indicator": "The Relative Strength Index (RSI) is a momentum oscillator that measures the speed and change of price movements.",
        "🧠 Options Basics": "Options are contracts that give the buyer the right, but not the obligation, to buy or sell an asset at a set price before a certain date."
    }

    for topic, content in sections.items():
        with st.expander(topic):
            st.write(content)
