from signal_overlay import get_recent_signals
def get_tone_drift():
    signals = get_recent_signals()
    mood_counts = {}
    for s in signals:
        mood_counts[s["mood"]] = mood_counts.get(s["mood"], 0) + 1
    total = sum(mood_counts.values())
    return {m: round(c/total,2) for m,c in mood_counts.items()}
