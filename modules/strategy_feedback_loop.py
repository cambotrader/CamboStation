belief_updates = []
def reinforce_agent_beliefs(agent_name, outcome):
    update = f"{timestamp_now()} ? {agent_name} belief {'strengthened' if outcome == 'win' else 'recalibrated'}"
    belief_updates.append(update)
    return belief_updates[-3:]
