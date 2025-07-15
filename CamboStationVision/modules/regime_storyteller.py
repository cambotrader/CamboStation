from signal_overlay import get_recent_signals

def narrate_regime():
    logs = get_recent_signals()
    lines = []

    if not logs:
        return ["📭 No regime detected — silence reigns."]

    for s in logs:
        regime = "Expansion" if s["conviction"] > 0.75 else "Consolidation"
        voice = f"🌀 {s['timestamp']} → {s['archetype']} held {regime} mood: **{s['mood']}**, conviction {s['conviction']}."
        tone = f"⚖️ Bias leaned toward {s['signal']}, shaped by emotion."
        lines.append(f"{voice}\n{tone}")

    return lines
