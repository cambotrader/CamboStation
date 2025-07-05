resolution_log = []
def resolve_conflict(ghost_vote, oracle_vote):
    if ghost_vote != oracle_vote:
        resolution = "Override engaged for hybrid consensus"
    else:
        resolution = "Unified conviction"
    resolution_log.append({
        "ghost": ghost_vote,
        "oracle": oracle_vote,
        "result": resolution,
        "timestamp": timestamp_now()
    })
    return resolution_log[-3:]
