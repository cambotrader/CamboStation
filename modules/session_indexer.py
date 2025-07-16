from signal_overlay import get_recent_signals

def index_session_tags():
    logs = get_recent_signals()
    tags = []
    for s in logs:
        regime = "Expansion" if s['conviction'] > 0.75 else "Consolidation"
        tag = f"[{regime}] {s['archetype']} | {s['mood']} | {s['signal']}"
        tags.append(tag)
    return tags
