codex_timeline = []
def log_belief_evolution(belief, timestamp, context):
    codex_timeline.append({"belief": belief, "timestamp": timestamp, "context": context})
def get_codex_timeline():
    return codex_timeline[-5:]
