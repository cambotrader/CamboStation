chart_patterns = [
    # === Bullish Reversal ===
    {
        "name": "Double Bottom",
        "group": "Bullish Reversal",
        "emoji": "🏗️",
        "description": "Two consecutive troughs at roughly the same price level after a downtrend, signaling reversal upward.",
        "trigger": "Two swing lows within 3-5% of each other + neckline breakout"
    },
    {
        "name": "Inverse Head and Shoulders",
        "group": "Bullish Reversal",
        "emoji": "🧍‍♂️⬇️🧍‍♂️",
        "description": "Three-trough pattern with a deeper middle valley (the 'head'), ends with breakout above neckline.",
        "trigger": "Left shoulder, deeper low, right shoulder symmetry + neckline break"
    },
    {
        "name": "Cup and Handle",
        "group": "Bullish Reversal",
        "emoji": "☕",
        "description": "Rounded U-shape bottom followed by a small pullback (handle), with breakout signaling strong bullish continuation.",
        "trigger": "Rounded base + shallow handle pullback <50% of cup height"
    },

    # === Bearish Reversal ===
    {
        "name": "Double Top",
        "group": "Bearish Reversal",
        "emoji": "🏔️",
        "description": "Two peaks near the same level followed by a drop below neckline. Indicates trend reversal down.",
        "trigger": "Two swing highs within 3-5% + neckline break down"
    },
    {
        "name": "Head and Shoulders",
        "group": "Bearish Reversal",
        "emoji": "🧍‍♂️⬆️🧍‍♂️",
        "description": "Three-peak formation with higher central peak (the 'head'). Typically precedes trend reversal.",
        "trigger": "Left shoulder, higher high, right shoulder symmetry + neckline breakdown"
    },
    {
        "name": "Rounding Top",
        "group": "Bearish Reversal",
        "emoji": "🌀",
        "description": "Gradual curve formation at the top of an uptrend, often signaling exhaustion and reversal.",
        "trigger": "Rounded top with declining volume and failed support retest"
    },

    # === Continuation ===
    {
        "name": "Bull Flag",
        "group": "Continuation",
        "emoji": "🚩",
        "description": "Small downward-sloping channel after a strong bullish impulse. Bullish breakout expected.",
        "trigger": "Impulse up ➜ downward channel ➜ breakout above resistance"
    },
    {
        "name": "Bear Flag",
        "group": "Continuation",
        "emoji": "🏴",
        "description": "Rising channel after a strong bearish impulse. Breakout expected to the downside.",
        "trigger": "Impulse down ➜ rising channel ➜ breakdown below support"
    },
    {
        "name": "Symmetrical Triangle",
        "group": "Continuation",
        "emoji": "🔺",
        "description": "Converging highs and lows. Directional breakout depends on trend context.",
        "trigger": "Higher lows + lower highs forming triangle ➜ breakout"
    },
    {
        "name": "Ascending Triangle",
        "group": "Continuation",
        "emoji": "📈",
        "description": "Flat top resistance with rising lows. Bullish pattern with breakout bias upward.",
        "trigger": "Equal highs + rising lows ➜ breakout above resistance"
    },
    {
        "name": "Descending Triangle",
        "group": "Continuation",
        "emoji": "📉",
        "description": "Flat support base with descending highs. Bearish breakdown likely.",
        "trigger": "Equal lows + lower highs ➜ breakdown"
    },

    # === Complex / Rare ===
    {
        "name": "Broadening Wedge",
        "group": "Complex",
        "emoji": "🔊",
        "description": "Price swings widen over time with higher highs and lower lows. Volatile and hard to trade.",
        "trigger": "Expanding highs/lows with volume spikes at ends"
    },
    {
        "name": "Diamond Top",
        "group": "Complex",
        "emoji": "💎",
        "description": "Symmetric structure with expanding then contracting prices. Often leads to reversal.",
        "trigger": "Broadening base ➜ narrowing exit ➜ breakdown"
    },
    {
        "name": "Megaphone",
        "group": "Complex",
        "emoji": "📣",
        "description": "Price expands upward and downward—like a megaphone. Signals volatility and eventual breakout.",
        "trigger": "Higher highs + lower lows expanding over time"
    }
]
