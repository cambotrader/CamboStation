def adjust_emotion(outcome):
    if outcome == "win":
        memory["recent_trade_mood"] = "confident"
    elif outcome == "loss":
        memory["recent_trade_mood"] = "reflective"
