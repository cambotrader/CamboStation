import json, os
from datetime import datetime

def compute_consistency_score():
    path = os.path.expandvars(r"$HOME\\CamboStation_QuantumOS\\modules\\myth_legacy.json")
    if not os.path.exists(path): return "No data."

    with open(path, "r", encoding="utf-8") as f:
        logs = json.load(f)

    dates = sorted(logs.keys())
    moods = []
    for d in dates:
        entry = logs[d].split("'")
        if len(entry) < 4: continue
        moods.append(entry[3])

    drift = sum(1 for i in range(1, len(moods)) if moods[i] != moods[i-1])
    variability = round((drift / max(1, len(moods)-1)) * 100, 2)
    score = 100 - variability

    return f"Identity Consistency Score: {score}%\nTonal Variability: {variability}%\nSessions: {len(moods)}"

if __name__ == "__main__":
    print(compute_consistency_score())

