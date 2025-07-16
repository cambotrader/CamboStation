def update_weights(trade_log):
    if recent_accuracy["pattern"] > recent_accuracy["sentiment"]:
        fusion_weights["pattern"] += 0.05
    else:
        fusion_weights["sentiment"] += 0.05
    normalize_weights(fusion_weights)
