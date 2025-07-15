from signal_overlay import get_recent_signals

def journal_signals():
    logs = get_recent_signals()
    entries = []
    for s in logs:
        arc = f"{s['timestamp']} → {s['archetype']} felt {s['mood'].lower()}, signaling {s['signal']} @ conviction {s['conviction']}"
        reflection = f"🧠 Mood: {s['mood']}. Emotion channels belief. Action reveals strategy."
        entries.append(f"{arc} · {reflection}")
    return entries
