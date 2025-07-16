drift_map = []
def simulate_drift(archetype, regime_shift):
    drift_map.append({
        "from": archetype,
        "to": regime_shift["preferred"],
        "volatility": regime_shift["vix"],
        "tone": regime_shift["mood"],
        "timestamp": timestamp_now()
    })
    return drift_map[-5:]
