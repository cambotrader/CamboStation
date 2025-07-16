narrative_state = {
    "voice": "Stoic Poet",
    "structure": "Belief ? Mood ? Action",
    "tone": "Clarity"
}
def rewrite_narrative(trade_outcomes):
    if trade_outcomes.count("loss") > 3:
        narrative_state["tone"] = "Cautious Introspection"
        narrative_state["voice"] = "Reflective Strategist"
    return narrative_state
