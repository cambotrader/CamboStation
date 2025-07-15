from signal_overlay import get_recent_signals

def compose_closing_stanza():
    logs = get_recent_signals()
    if not logs:
        return "⚪ No reflection offered — the session left no imprint."

    final = logs[-1]
    archetype = final["archetype"]
    mood = final["mood"]
    signal = final["signal"]
    conviction = final["conviction"]

    regime = "Expansion" if conviction > 0.75 else "Consolidation"

    motifs = {
        "Expansion": "winds widen across belief’s contour",
        "Consolidation": "silence binds tension beneath formation"
    }

    tone_line = f"The {archetype} moved in **{mood.lower()}** tone, casting `{signal}` with conviction `{conviction}`."
    motif_line = f"As the regime closed in **{regime}**, {motifs[regime]}."

    stanza = f"🪶 {tone_line}\n{motif_line}\nThus, the day folds beneath emotional weather."
    return stanza
