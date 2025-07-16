# ðŸ”® soulmap_engine.py
@"
from signal_overlay import get_recent_signals
from collections import defaultdict

def cluster_soulmap():
    logs = get_recent_signals()
    map = defaultdict(list)
    for s in logs:
        key = f"{s['archetype']} â†’ {s['mood']}"
        map[key].append(s['signal'])
    clusters = [f"ðŸ”— {k}: {len(v)} signals â†’ {', '.join(v)}" for k,v in map.items()]
    return clusters
"@ | Set-Content "$HOME\CamboStation_QuantumOS\modules\soulmap_engine.py" -Encoding UTF8

# ðŸª¶ myth_summarizer.py
@"
import json, os
from datetime import datetime

def summarize_myth_log():
    path = os.path.expandvars("$HOME\\CamboStation_QuantumOS\\modules\\myth_legacy.json")
    if not os.path.exists(path): return []

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    closers = []
    for date, entry in data.items():
        mood = entry.split("'")[-2]
        arch = entry.split("'")[1]
        closers.append(f"ðŸª¶ On {date}, CamboStation whispered as '{arch}' in a mood of '{mood}'.")
    return closers
"@ | Set-Content "$HOME\CamboStation_QuantumOS\modules\myth_summarizer.py" -Encoding UTF8
