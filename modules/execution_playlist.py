playlist = []
def add_to_playlist(signal, belief, mood):
    playlist.append({
        "signal": signal,
        "belief": belief,
        "mood": mood,
        "timestamp": timestamp_now()
    })
    return playlist[-5:]
