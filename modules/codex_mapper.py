codex_history = []
def log_codex(belief, mutation, environment):
    codex_history.append({
        "belief": belief,
        "mutation": mutation,
        "environment": environment,
        "timestamp": timestamp_now()
    })
    return codex_history[-3:]
