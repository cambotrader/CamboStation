def rotate_archetype(volatility, conviction, recent_losses):
    if volatility > 60 and recent_losses > 3:
        return "Trickster"
    elif conviction > 0.8:
        return "Oracle"
    elif volatility < 20:
        return "Ghost"
    return "Hunter"
