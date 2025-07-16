# Strategy Linker Module — CamboStation™
# Converts detected patterns into strategy ideas

def link_detected_patterns_to_strategy(detected_patterns):
    strategy_signals = []

    for date, pattern in detected_patterns:
        strategy = None
        comment = ""

        if pattern == "Head & Shoulders":
            strategy = "Short Reversal"
            comment = "Break below neckline signals bearish setup"

        elif pattern == "Double Top":
            strategy = "Short Rejection Setup"
            comment = "Resistance retested — breakout failure"

        elif pattern == "Double Bottom":
            strategy = "Long Reversal Entry"
            comment = "Support confirmed — momentum likely"

        elif pattern == "Ascending Triangle":
            strategy = "Breakout Strategy (Long)"
            comment = "Higher lows squeezing against resistance"

        elif pattern == "Descending Triangle":
            strategy = "Breakout Strategy (Short)"
            comment = "Lower highs compressing — bearish breakout expected"

        elif pattern == "Falling Wedge":
            strategy = "Momentum Reversal (Long)"
            comment = "Tapering volatility — upside breakout probable"

        elif pattern == "Rising Wedge":
            strategy = "Momentum Reversal (Short)"
            comment = "Bearish divergence building in narrowing trend"

        # Add more mapping logic here...

        if strategy:
            strategy_signals.append({
                "date": date,
                "pattern": pattern,
                "strategy": strategy,
                "comment": comment
            })

    return strategy_signals
