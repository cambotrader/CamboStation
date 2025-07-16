def render():
    if sentiment_tone == "quiet" and not pattern_noise:
        signal = "BUY"; mood = "Whisper Clarity"
    elif fusion_confidence < 0.3:
        signal = "PASS"; mood = "Silent Resistance"
    log_trade(signal, "Ghost", mood)
