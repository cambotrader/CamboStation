def assess_fate(signal, market_state):
    if signal == "BUY" and market_state == "chaotic": return "delay"
    elif signal == "SELL" and market_volatility < 20: return "dismiss"
    return "allow"
