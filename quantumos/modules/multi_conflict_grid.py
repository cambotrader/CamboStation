conflict_zones = []
def simulate_multi_conflict(archetype_set, signals):
    verdict = "harmonic fusion" if len(set(signals)) == 1 else "ideological split"
    conflict_zones.append({
        "archetypes": archetype_set,
        "signals": signals,
        "verdict": verdict,
        "timestamp": timestamp_now()
    })
    return conflict_zones[-1]
