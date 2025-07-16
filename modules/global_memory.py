memory = {
    "recent_trade_mood": "reflective",
    "active_archetype": "Oracle",
    "conviction_level": 0.83,
    "override_tension": "low",
    "trade_stress_index": 27,
    "belief_shift": []
}
def update(key, value): memory[key] = value
def recall(key): return memory.get(key)
