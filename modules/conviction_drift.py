drift_log = []
def track_drift(old_codex, new_codex):
    changes = set(new_codex) - set(old_codex)
    drift_log.append({"timestamp": timestamp_now(), "drift": list(changes)})
    return drift_log
