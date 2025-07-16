from signal_overlay import get_recent_signals
def compose_beliefs():
    signals = get_recent_signals()
    output = []
    for s in signals:
        mood = s["mood"]
        signal = s["signal"]
        archetype = s["archetype"]
        belief = f"Conviction behind {signal} reflects {mood.lower()} resolve of the {archetype}."
        output.append(belief)
    return output
