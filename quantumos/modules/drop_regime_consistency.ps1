# Create regime_tracker.py
@"
import json, os
from collections import defaultdict, Counter
from datetime import datetime

def load_legacy():
    path = os.path.expandvars("$HOME\\CamboStation_QuantumOS\\modules\\myth_legacy.json")
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
        output.append(f"{period} → {top[0]} ({top[1]} sessions)")
    return output

if __name__ == "__main__":
    for line in track_regimes():
        print(line)
"@ | Set-Content "$HOME\CamboStation_QuantumOS\modules\regime_tracker.py" -Encoding UTF8

# Create identity_consistency_score.py
@"
import json, os
from datetime import datetime

def compute_consistency_score():
    path = os.path.expandvars("$HOME\\CamboStation_QuantumOS\\modules\\myth_legacy.json")
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
"@ | Set-Content "$HOME\CamboStation_QuantumOS\modules\identity_consistency_score.py" -Encoding UTF8

# Wire cockpit modes 25 and 26
$cockpitPath = "$HOME\CamboStation_QuantumOS\modules\cockpit.ps1"
$content = Get-Content $cockpitPath -Raw

if ($content -match '\$cmds\s*=\s*@\([^\)]*') {
    $content = $content -replace '(\$cmds\s*=\s*@\([^\)]*)', '$1,"regime tracker","consistency score"'
}

$patch = @"
    "regime tracker"      { python "$base\regime_tracker.py" }
    "consistency score"   { python "$base\identity_consistency_score.py" }
"@

if ($content -notmatch '"regime tracker"') {
    $content += "`n$patch"
}

Set-Content $cockpitPath -Value $content -Encoding UTF8
Write-Host "Modes 25 and 26 wired successfully."
