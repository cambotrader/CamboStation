signal_map = []
def log_signal(signal, archetype, mood, belief):
    signal_map.append({
        "signal": signal,
        "archetype": archetype,
        "mood": mood,
        "belief": belief
    })
def get_grid():
    return signal_map[-10:]
