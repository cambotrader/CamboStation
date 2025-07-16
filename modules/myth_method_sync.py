codex_sync = []
def sync_codex_to_action(belief, module_triggered):
    codex_sync.append({
        "belief": belief,
        "method": module_triggered,
        "timestamp": timestamp_now()
    })
    return codex_sync[-3:]
