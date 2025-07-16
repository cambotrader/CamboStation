from signal_overlay import get_recent_signals
def generate_myth():
    signals = get_recent_signals()
    storyline = ["In the beginning, the Oracle foresaw divergence."]
    for s in signals:
        fragment = f"The {s['archetype']} rose in {s['mood']} silence, casting a {s['signal']} into the stream â€” conviction at {s['conviction']}."
        storyline.append(fragment)
    storyline.append("Thus the session closed, signaling truth beyond tension.")
    return storyline
