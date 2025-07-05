harmonic_log = []
def log_harmonic(signal, emotion, outcome):
    harmonic_log.append({
        "signal": signal,
        "emotion": emotion,
        "outcome": outcome,
        "tone": "resonant" if outcome == "win" else "fractured"
    })
    return harmonic_log[-5:]
