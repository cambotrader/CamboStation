forecast_log = []
def forecast_drift(current_tone, trade_mood, emotional_tension):
    next_state = "Oracle" if emotional_tension > 70 else "Ghost"
    forecast_log.append({
        "from": current_tone,
        "to": next_state,
        "mood": trade_mood,
        "tension": emotional_tension,
        "timestamp": timestamp_now()
    })
    return forecast_log[-1]
