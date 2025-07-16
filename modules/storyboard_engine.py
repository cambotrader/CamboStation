storyboard_log = []
def record_scene(signal, archetype, mood, result):
    storyboard_log.append({
        "scene": f"{archetype} enacted {signal} with {mood} ? {result}",
        "timestamp": timestamp_now()
    })
    return storyboard_log[-3:]
