personality_state = {
    "voice_tone": "neutral",
    "risk_bias": "moderate",
    "mood_cycle": ["reflective", "confident"]
}
def evolve_personality(trade_result):
    if trade_result == "loss":
        personality_state["voice_tone"] = "cautious"
        personality_state["risk_bias"] = "low"
    elif trade_result == "win":
        personality_state["voice_tone"] = "optimistic"
        personality_state["risk_bias"] = "high"
    return personality_state
