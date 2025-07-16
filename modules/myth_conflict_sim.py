conflict_outcomes = []
def simulate_conflict(ghost_vote, oracle_vote):
    if ghost_vote == oracle_vote:
        verdict = "unified strategy"
    else:
        verdict = "internal discord"
    conflict_outcomes.append({
        "ghost": ghost_vote,
        "oracle": oracle_vote,
        "verdict": verdict,
        "timestamp": timestamp_now()
    })
    return conflict_outcomes[-1]
