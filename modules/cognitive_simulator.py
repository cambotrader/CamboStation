sim_results = []
def simulate_scenario(archetype, mood, volatility, signal):
    result = {
        "archetype": archetype,
        "mood": mood,
        "volatility": volatility,
        "signal": signal,
        "performance": f"Simulated outcome under {archetype}-{mood} at VIX {volatility}"
    }
    sim_results.append(result)
    return sim_results[-3:]
