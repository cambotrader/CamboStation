def harmonize(sentiment_ext, mood_internal):
    if sentiment_ext == "bullish" and mood_internal == "fear":
        return "BLOCK"
    elif sentiment_ext == mood_internal:
        return "ALIGN"
    return "CAUTION"
