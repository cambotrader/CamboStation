reinforcement_log = []
def reinforce_belief(trade, outcome, conviction_score):
    if outcome == "win" and conviction_score > 0.8:
        reinforcement_log.append(f"{timestamp_now()} ? Reinforced: {trade['belief']}")
    return reinforcement_log[-3:]
