from signal_overlay import get_recent_signals

def narrate_session():
    logs = get_recent_signals()
    lines = []

    for s in logs:
        archetype = s["archetype"]
        mood = s["mood"]
        signal = s["signal"]
        conviction = s["conviction"]

        if conviction > 0.75:
            sentiment = "with unwavering intent"
        elif conviction > 0.65:
            sentiment = "guided by quiet confidence"
        else:
            sentiment = "tentative yet reflective"

        line = f"🕒 {s['timestamp']} → The {archetype}, {mood.lower()} and alert, cast a {signal} {sentiment}. Conviction scored at {conviction}."
        lines.append(line)

    if not lines:
        lines.append("📭 No signals detected — silence speaks louder today.")

    return lines
