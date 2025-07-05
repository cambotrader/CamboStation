# ðŸ“ˆ myth_index_plot.py
@"
import json
import matplotlib.pyplot as plt
import os

def plot_myth_volatility():
    path = os.path.expandvars("$HOME\\CamboStation_QuantumOS\\modules\\myth_legacy.json")
    if not os.path.exists(path): return

    with open(path, "r", encoding="utf-8") as f:
        logs = json.load(f)

    dates = sorted(logs.keys())
    moods = []
    for date in dates:
        mood = logs[date].split("'")[-2]
        moods.append(mood)

    # Encode mood as integers
    mood_set = sorted(set(moods))
    mood_map = {m: i for i, m in enumerate(mood_set)}
    mood_vals = [mood_map[m] for m in moods]

    plt.figure(figsize=(10, 4))
    plt.plot(dates, mood_vals, marker='o', color='blue', linewidth=2)
    plt.title("ðŸª CamboStation Mood Volatility")
    plt.xticks(rotation=45)
    plt.yticks(list(mood_map.values()), list(mood_map.keys()))
    plt.tight_layout()
    plt.grid(True)
    plt.show()
"@ | Set-Content "$HOME\CamboStation_QuantumOS\modules\myth_index_plot.py" -Encoding UTF8

# ðŸ” identity_drift_analyzer.py
@"
import json
import os
from collections import defaultdict
from datetime import datetime, timedelta

def get_week_label(date_str):
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    week_start = dt - timedelta(days=dt.weekday())
    return week_start.strftime("%Y-%m-%d")

def analyze_identity_drift():
    path = os.path.expandvars("$HOME\\CamboStation_QuantumOS\\modules\\myth_legacy.json")
    if not os.path.exists(path): return []

    with open(path, "r", encoding="utf-8") as f:
        logs = json.load(f)

    drift = defaultdict(set)
    for date, entry in logs.items():
        week = get_week_label(date)
        parts = entry.split("'")
        if len(parts) < 4: continue
        mood = parts[3]
        arch = parts[1]
        drift[week].add(f"{arch}:{mood}")

    output = []
    weeks = sorted(drift.keys())
    for w in weeks:
        cluster = ", ".join(drift[w])
        output.append(f"ðŸ“… {w}: {cluster}")
    return output
"@ | Set-Content "$HOME\CamboStation_QuantumOS\modules\identity_drift_analyzer.py" -Encoding UTF8
