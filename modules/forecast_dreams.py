dream_log = []
def log_forecast(archetype, mood, signal):
    dream_log.append({
        "timestamp": timestamp_now(),
        "archetype": archetype,
        "mood": mood,
        "signal": signal
    })
def recall_dreams():
    return dream_log[-5:]
