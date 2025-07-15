import streamlit as st

def alert(signal, confidence):
    if signal.lower() == "buy" and confidence >= 0.75:
        st.success(f"🟢 BUY Signal Alert – Confidence {confidence}")
    elif signal.lower() == "sell" and confidence >= 0.75:
        st.error(f"🔴 SELL Signal Alert – Confidence {confidence}")
    else:
        st.warning(f"⚠️ Mixed or Neutral Vote Detected – Confidence {confidence}")
