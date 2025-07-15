import json, os
from datetime import datetime

# Import your identity synthesis engine (replace with actual module if different)
try:
    from identity_myth_engine import synthesize_identity_myth
except ImportError:
    def synthesize_identity_myth():
        return "The Oracle felt a sense of clarity and proclaimed 'Joy' through the mythstream."

def log_myth_today():
    path = os.path.join(os.path.expanduser("~"), "CamboStation_QuantumOS", "modules", "myth_legacy.json")

    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            logs = json.load(f)
    else:
        logs = {}

    today = datetime.today().strftime("%Y-%m-%d")
    logs[today] = synthesize_identity_myth()

    with open(path, "w", encoding="utf-8") as f:
        json.dump(logs, f, indent=2, ensure_ascii=False)

    print(f"✅ Myth snapshot logged for {today}")
