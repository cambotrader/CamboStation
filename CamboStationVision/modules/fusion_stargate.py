fusion_entities = []
def create_fusion(archetypes, signals, tone):
    fusion_entities.append({
        "archetypes": archetypes,
        "signals": signals,
        "tone": tone,
        "timestamp": timestamp_now()
    })
    return fusion_entities[-1]
