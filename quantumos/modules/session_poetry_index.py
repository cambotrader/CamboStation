from signal_overlay import get_recent_signals

def build_poetry_index():
    logs = get_recent_signals()
    archive = []

    for s in logs:
        regime = "Expansion" if s["conviction"] > 0.75 else "Consolidation"
        line = f"🪶 [{regime}] The {s['archetype']} felt {s['mood'].lower()}, signaling {s['signal']} @ conviction {s['conviction']}"
        archive.append(line)

    return archive
