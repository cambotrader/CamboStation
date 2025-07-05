from signal_overlay import get_recent_signals

def generate_session_summary():
    logs = get_recent_signals()
    if not logs:
        return {
            "voice": "🕊️ No signals registered. The field remains quiet.",
            "mood_counts": {},
            "conviction_avg": 0,
            "regime": "None"
        }

    moods = {}
    total_conviction = 0
    for s in logs:
        mood = s["mood"]
        moods[mood] = moods.get(mood, 0) + 1
        total_conviction += s["conviction"]

    avg_conviction = round(total_conviction / len(logs), 2)

    regime = "Expansion" if avg_conviction > 0.75 else "Consolidation"

    dominant_mood = max(moods.items(), key=lambda x: x[1])[0]
    voice = f"📊 Dominant mood: **{dominant_mood}** | Avg conviction: `{avg_conviction}` | Regime: **{regime}**"

    return {
        "voice": voice,
        "mood_counts": moods,
        "conviction_avg": avg_conviction,
        "regime": regime
    }
