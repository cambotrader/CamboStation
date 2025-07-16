def determine_priority(agents):
    sorted_agents = sorted(agents, key=lambda x: (x["conviction"], x["accuracy"]), reverse=True)
    return [a["name"] for a in sorted_agents]
