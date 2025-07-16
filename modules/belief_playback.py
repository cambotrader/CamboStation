def replay_beliefs():
    history = memory["belief_shift"]
    for entry in history:
        print(f"??? {entry['timestamp']} ? Belief Drift: {entry['drift']}")
