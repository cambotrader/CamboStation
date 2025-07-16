harmonics_map = []
def calculate_harmonics(belief_strengths):
    avg = sum(belief_strengths) / len(belief_strengths)
    tone = "resonant" if avg > 0.75 else "uncertain"
    harmonics_map.append({"average": avg, "tone": tone})
    return harmonics_map[-1]
