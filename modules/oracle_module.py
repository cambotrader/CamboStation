def render():
    if fusion_confidence > 0.75 and sentiment_tone == "calm":
        signal = "BUY"; mood = "Cautious Clarity"
    elif fusion_confidence < 0.35 and pattern_divergence:
        signal = "SELL"; mood = "Pattern Warning"
    log_trade(signal, "Oracle", mood)
