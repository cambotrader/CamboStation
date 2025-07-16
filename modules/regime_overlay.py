regime_snapshots = []
def capture_regime(mood, sentiment_ext, archetype, volume):
    regime_snapshots.append({
        "mood": mood,
        "sentiment": sentiment_ext,
        "persona": archetype,
        "volume": volume,
        "timestamp": timestamp_now()
    })
def recent_snapshots(): return regime_snapshots[-5:]
