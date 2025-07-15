import json
import os
from collections import Counter
from datetime import datetime

def compute_myth_index():
    path = os.path.expandvars("$HOME\\CamboStation_QuantumOS\\modules\\myth_legacy.json")
    if not os.path.exists(path):
        return "❌ No legacy data found."

    with open(path, "r", encoding="utf-8") as f:
        logs = json.load(f)

    mood_variability = 0
    mood_list = []
    archetype_list = []

    dates = sorted(logs.keys())
    prev_mood = None

    for date in dates:
        entry = logs[date]
        parts = entry.split("'")
        if len(parts) < 4: continue
        archetype = parts[1]
        mood = parts[3]
        mood_list.append(mood)
        archetype_list.append(archetype)

        if prev_mood is not None and prev_mood != mood:
            mood_variability += 1
        prev_mood = mood

    mood_vol = round(mood_variability / max(1, len(dates) - 1), 2)
    arch_freq = Counter(archetype_list)
    dominant_arch = arch_freq.most_common(1)[0][0] if arch_freq else "Unknown"

    summary = f"""
📊 Myth Index Score
---------------------
🪐 Mood Volatility     → {mood_vol * 100:.0f}% variation
🔮 Dominant Archetype  → {dominant_arch}
📆 Sessions Analyzed   → {len(dates)}
🎯 Archetype Spread    → {dict(arch_freq)}

✅ Interpretation:
- High volatility may indicate system drift or emotional instability.
- Low volatility suggests tonal consistency or archetypal fixation.
"""

    return summary.strip()

# Run directly
if __name__ == "__main__":
    print(compute_myth_index())
