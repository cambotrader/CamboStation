from signal_overlay import get_recent_signals

def myth_voice():
    logs = get_recent_signals()
    if not logs:
        return "⚪ The void holds no echo. Silence remains unbroken."

    last = logs[-1]
    mood = last["mood"]
    archetype = last["archetype"]
    signal = last["signal"]
    conviction = last["conviction"]

    themes = {
        "Expansion": "the regime breathes onward",
        "Consolidation": "the axis narrows, awaiting divergence"
    }

    regime = "Expansion" if conviction > 0.75 else "Consolidation"
    motif = themes[regime]

    tone = f"The {archetype}, {mood.lower()} in stance, cast a final {signal} at `{conviction}` conviction."
    voice = f"🪶 As dusk fell, {motif}. {tone}"

    return voice
