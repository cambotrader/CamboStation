import json, os
from collections import defaultdict, Counter
from datetime import datetime

def load_legacy():
    path = os.path.expandvars("C:\Users\johnl\\CamboStation_QuantumOS\\modules\\myth_legacy.json")
    return json.load(open(path, "r", encoding="utf-8")) if os.path.exists(path) else {}

def get_period(date_str, mode="month"):
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    return dt.strftime("%Y-%m") if mode == "month" else dt.strftime("%Y-W%U")

def track_regimes():
    logs = load_legacy()
    by_period = defaultdict(list)

    for date, entry in logs.items():
        parts = entry.split("'")
        if len(parts) < 4: continue
        arch, mood = parts[1], parts[3]
        label = f"{arch}:{mood}"
        period = get_period(date)
        by_period[period].append(label)

    output = []
    for period in sorted(by_period):
        freq = Counter(by_period[period])
        top = freq.most_common(1)[0]
        output.append(f"{period} â†’ {top[0]} ({top[1]} sessions)")
    return output

if __name__ == "__main__":
    for line in track_regimes():
        print(line)
