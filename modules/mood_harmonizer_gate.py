from mood_harmonizer import harmonize
alignment = harmonize(sentiment_external, memory["recent_trade_mood"])
if alignment == "BLOCK":
    st.warning("? Emotional conflict detected. Trade blocked.")
    return
