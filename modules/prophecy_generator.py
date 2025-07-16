prophecy_log = []
def generate_prophecy(belief, mood, previous_outcome):
    vision = f"Forecast: If mood is '{mood}', belief '{belief}' will lead to {'victory' if previous_outcome == 'win' else 'risk'}"
    prophecy_log.append(vision)
    return prophecy_log[-3:]
