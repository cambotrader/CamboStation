def execute_team_signal(agent_votes):
    votes = {}
    for agent, signal in agent_votes.items():
        votes[signal] = votes.get(signal, 0) + 1
    return max(votes, key=votes.get)
