candlestick_definitions = [
    # === Bullish ===
    {
        "name": "Hammer",
        "group": "Bullish",
        "emoji": "🔨",
        "description": "A small-bodied candle with a long lower shadow, often after a downtrend.",
        "trigger": "Body < 30% of total range, long lower wick",
        "show_on_chart": True
    },
    {
        "name": "Inverted Hammer",
        "group": "Bullish",
        "emoji": "🪞",
        "description": "A small body with a long upper shadow, possible reversal after a downtrend.",
        "trigger": "Small body near bottom + long upper wick",
        "show_on_chart": True
    },
    {
        "name": "Bullish Engulfing",
        "group": "Bullish",
        "emoji": "🟢",
        "description": "A green candle completely engulfs the previous red candle.",
        "trigger": "Green body fully contains prior red candle body",
        "show_on_chart": True
    },
    {
        "name": "Morning Star",
        "group": "Bullish",
        "emoji": "🌅",
        "description": "Three candle reversal pattern: red ➜ indecision ➜ strong green.",
        "trigger": "Down candle, doji/small candle, large up candle closing above midpoint",
        "show_on_chart": True
    },
    {
        "name": "Tweezer Bottom",
        "group": "Bullish",
        "emoji": "👣",
        "description": "Two candles with nearly equal lows after a decline.",
        "trigger": "Lows match within ~1% + shift from red to green",
        "show_on_chart": True
    },

    # === Bearish ===
    {
        "name": "Hanging Man",
        "group": "Bearish",
        "emoji": "🚶",
        "description": "Looks like a hammer but appears after an uptrend—bearish signal.",
        "trigger": "Small body on top + long lower wick after uptrend",
        "show_on_chart": True
    },
    {
        "name": "Shooting Star",
        "group": "Bearish",
        "emoji": "💫",
        "description": "Small body near bottom, long upper shadow, warning of reversal.",
        "trigger": "Long upper wick > 2x body after uptrend",
        "show_on_chart": True
    },
    {
        "name": "Bearish Engulfing",
        "group": "Bearish",
        "emoji": "🔴",
        "description": "A red candle completely engulfs the previous green candle.",
        "trigger": "Red body fully contains prior green candle body",
        "show_on_chart": True
    },
    {
        "name": "Evening Star",
        "group": "Bearish",
        "emoji": "🌆",
        "description": "Green ➜ indecision ➜ large red candle closing below midpoint.",
        "trigger": "Up candle, doji/small, red closing below midpoint of first",
        "show_on_chart": True
    },
    {
        "name": "Tweezer Top",
        "group": "Bearish",
        "emoji": "🔼",
        "description": "Two candles with nearly equal highs at resistance.",
        "trigger": "Highs match within ~1% + shift from green to red",
        "show_on_chart": True
    },

    # === Neutral / Indecision ===
    {
        "name": "Doji",
        "group": "Neutral",
        "emoji": "⚖️",
        "description": "Open and close are very close—signals market indecision.",
        "trigger": "Body < 5% of total candle range",
        "show_on_chart": True
    },
    {
        "name": "Spinning Top",
        "group": "Neutral",
        "emoji": "🌀",
        "description": "Small body with equal upper/lower wicks—uncertainty.",
        "trigger": "Small body, similar sized wicks",
        "show_on_chart": True
    },
    {
        "name": "Long-Legged Doji",
        "group": "Neutral",
        "emoji": "🦵",
        "description": "Extreme indecision: very long wicks, tiny body.",
        "trigger": "Body ~zero + long upper & lower wicks",
        "show_on_chart": True
    },

    # === Continuation ===
    {
        "name": "Rising Three",
        "group": "Continuation",
        "emoji": "🔺",
        "description": "Big green candle ➜ 3 small red ➜ new green closing higher.",
        "trigger": "Bull candle → 3 reds inside → new green closing above first",
        "show_on_chart": True
    },
    {
        "name": "Falling Three",
        "group": "Continuation",
        "emoji": "🔻",
        "description": "Big red ➜ 3 small greens ➜ red breakdown candle.",
        "trigger": "Bear candle → 3 greens → breakdown red",
        "show_on_chart": True
    },
    {
        "name": "Side-by-Side White Lines",
        "group": "Continuation",
        "emoji": "📏",
        "description": "Two or more equal length green candles confirming trend.",
        "trigger": "Consecutive similar-sized bullish candles",
        "show_on_chart": True
    },

    # === Complex / Rare ===
    {
        "name": "Abandoned Baby",
        "group": "Complex",
        "emoji": "👶",
        "description": "Gap down → Doji → gap up. Rare bullish reversal.",
        "trigger": "Down gap, isolated doji, up gap",
        "show_on_chart": True
    },
    {
        "name": "Deliberation",
        "group": "Complex",
        "emoji": "🤔",
        "description": "Three green candles → rising tension → risk of bearish shift.",
        "trigger": "3 up candles, weakening 3rd body",
        "show_on_chart": True
    },
    {
        "name": "Stick Sandwich",
        "group": "Complex",
        "emoji": "🥪",
        "description": "Bear → Bull → Bear with identical closes. Potential reversal.",
        "trigger": "Matching close on candle 1 & 3 sandwiching a green",
        "show_on_chart": True
    },
    {
        "name": "Ladder Bottom",
        "group": "Complex",
        "emoji": "🪜",
        "description": "Series of 3 or more declining candles followed by reversal green.",
        "trigger": "3+ lower closes → final strong green candle",
        "show_on_chart": True
    }
]
