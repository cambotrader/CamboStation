mutated_codex = []
def mutate_codex_entry(belief, outcome, environment):
    if outcome == "loss" and environment == "uncertain":
        mutation = f"{belief} ? Drifted to 'Restraint before rhythm'"
    else:
        mutation = f"{belief} ? Reinforced"
    mutated_codex.append({"original": belief, "mutation": mutation, "timestamp": timestamp_now()})
    return mutated_codex[-3:]
