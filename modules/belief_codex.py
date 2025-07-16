def update_beliefs(trade_outcome):
    if trade_outcome == "win":
        reinforce("Conviction must earn execution")
    elif trade_outcome == "loss":
        adjust("Bias is a mirror, not a compass")
