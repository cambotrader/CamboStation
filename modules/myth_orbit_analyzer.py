from signal_overlay import get_recent_signals
from collections import defaultdict

def analyze_myth_orbit():
    logs = get_recent_signals()
    archive = defaultdict(list)
    for s in logs:
        tone = "Expansion" if s['conviction'] > 0.75 else "Consolidation"
        arc = f"🪐 {s['archetype']} drifted through {s['mood']} → {s['signal']} ({tone}) @ {s['conviction']}"
        archive[tone].append(arc)
    output = []
    for regime, lines in archive.items():
        output.append(f"## 🔮 Myth Cycle: {regime}")
        output.extend(lines)
    return output
