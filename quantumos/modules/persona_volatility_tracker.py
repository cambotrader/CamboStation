volatility_map = []
def track_volatility(archetype, delta_vix, outcome):
    volatility_map.append({
        "archetype": archetype,
        "delta": delta_vix,
        "outcome": outcome,
        "timestamp": timestamp_now()
    })
def recent_volatility(): return volatility_map[-5:]
