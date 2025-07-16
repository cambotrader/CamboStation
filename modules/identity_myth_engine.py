from signal_overlay import get_recent_signals
from collections import Counter

def synthesize_identity_myth():
    logs = get_recent_signals()
    archetypes = [s['archetype'] for s in logs]
    moods = [s['mood'] for s in logs]
    if not archetypes or not moods:
        return "🌌 CamboStation has not yet spoken often enough to form identity."

    dominant_archetype = Counter(archetypes).most_common(1)[0]
    dominant_mood = Counter(moods).most_common(1)[0]
    return f"🌌 CamboStation speaks most often as '{dominant_archetype[0]}' in a mood of '{dominant_mood[0]}'"
