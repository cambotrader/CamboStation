def publish_story(signal, archetype, mood):
    entry = f"CamboStation acted: {signal} via {archetype} in {mood}"
    saga_log.append(entry)
    stylize_into_poem(entry)
    update_visual_canvas(entry)
