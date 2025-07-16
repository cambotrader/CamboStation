def playback_epoch(regime_logs):
    return [f"{r['timestamp']} | {r['archetype']} | Mood: {r['mood']} | VIX: {r['volatility']}" for r in regime_logs[-5:]]
