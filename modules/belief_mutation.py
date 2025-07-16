belief_codex = ["Conviction earns execution", "Bias mirrors truth"]
def mutate(outcomes):
    for trade in outcomes:
        if trade["loss"]: belief_codex.append("Restraint precedes precision")
    return belief_codex
