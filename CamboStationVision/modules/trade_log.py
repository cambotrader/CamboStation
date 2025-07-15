import json, os, datetime

def log_trade(asset, signal, confidence, outcome):
    log_entry = {
        "timestamp": datetime.datetime.now().isoformat(),
        "asset": asset,
        "signal": signal,
        "confidence": confidence,
        "outcome": outcome
    }

    logs_dir = os.path.join(os.path.dirname(__file__), "..", "logs")
    os.makedirs(logs_dir, exist_ok=True)
    log_file = os.path.join(logs_dir, "voting_history.json")

    if os.path.exists(log_file):
        with open(log_file, "r", encoding="utf-8") as f:
            history = json.load(f)
    else:
        history = []

    history.append(log_entry)

    with open(log_file, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2)
