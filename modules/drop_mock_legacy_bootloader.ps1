@"
import json, os
from datetime import datetime, timedelta
import random

def synth_myth(archetypes, moods):
    arch = random.choice(archetypes)
    mood = random.choice(moods)
    return f"The {arch} felt a shift and proclaimed '{mood}' through the mythstream."

def drop_mock_legacy():
    path = os.path.join(os.path.expanduser("~"), "CamboStation_QuantumOS", "modules", "myth_legacy.json")
    logs = {}

    archetypes = ["Oracle", "Ghost", "Trickster", "Hero", "Seeker"]
    moods = ["Joy", "Anxiety", "Conviction", "Curiosity", "Melancholy"]

    for i in range(7):
        dt = (datetime.today() - timedelta(days=i)).strftime("%Y-%m-%d")
        logs[dt] = synth_myth(archetypes, moods)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(logs, f, indent=2, ensure_ascii=False)

    print("✅ Mock legacy injected with 7 synthetic myth entries.")

if __name__ == "__main__":
    drop_mock_legacy()
"@ | Set-Content "$HOME\CamboStation_QuantumOS\modules\mock_legacy_bootloader.py" -Encoding UTF8
