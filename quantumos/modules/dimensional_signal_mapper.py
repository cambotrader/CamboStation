signal_grid = []
def map_signal(signal, archetype, volatility, mood, timestamp):
    signal_grid.append({
        "signal": signal,
        "archetype": archetype,
        "volatility": volatility,
        "mood": mood,
        "timestamp": timestamp
    })
def last_signals(n=5): return signal_grid[-n:]
