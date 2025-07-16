import pandas as pd

def detect_chart_patterns(df, pattern_settings):
    matches = []

    for pattern_name, config in pattern_settings.items():
        if not config.get("enabled", False):
            continue

        if pattern_name == "Double Top":
            for i in range(2, len(df) - 2):
                highs = df["High"]
                if (
                    abs(highs[i] - highs[i - 2]) / highs[i] < 0.03 and
                    highs[i] > highs[i - 1] and
                    highs[i - 2] > highs[i - 3] and
                    df["Close"].iloc[i + 1] < (highs[i] + highs[i - 2]) / 2
                ):
                    matches.append({"pattern": pattern_name, "index": i, "emoji": config["emoji"]})

        elif pattern_name == "Double Bottom":
            for i in range(2, len(df) - 2):
                lows = df["Low"]
                if (
                    abs(lows[i] - lows[i - 2]) / lows[i] < 0.03 and
                    lows[i] < lows[i - 1] and
                    lows[i - 2] < lows[i - 3] and
                    df["Close"].iloc[i + 1] > (lows[i] + lows[i - 2]) / 2
                ):
                    matches.append({"pattern": pattern_name, "index": i, "emoji": config["emoji"]})

        elif pattern_name == "Bull Flag":
            for i in range(5, len(df)):
                impulse = df["Close"].iloc[i - 5] < df["Close"].iloc[i - 4]
                flag = df["Close"].iloc[i - 3] > df["Close"].iloc[i - 2] > df["Close"].iloc[i - 1]
                breakout = df["Close"].iloc[i] > df["Close"].iloc[i - 4]
                if impulse and flag and breakout:
                    matches.append({"pattern": pattern_name, "index": i, "emoji": config["emoji"]})

        elif pattern_name == "Bear Flag":
            for i in range(5, len(df)):
                impulse = df["Close"].iloc[i - 5] > df["Close"].iloc[i - 4]
                flag = df["Close"].iloc[i - 3] < df["Close"].iloc[i - 2] < df["Close"].iloc[i - 1]
                breakdown = df["Close"].iloc[i] < df["Close"].iloc[i - 4]
                if impulse and flag and breakdown:
                    matches.append({"pattern": pattern_name, "index": i, "emoji": config["emoji"]})

        elif pattern_name == "Symmetrical Triangle":
            for i in range(10, len(df) - 1):
                recent_highs = df["High"].iloc[i - 5:i]
                recent_lows = df["Low"].iloc[i - 5:i]
                if (
                    recent_highs.is_monotonic_decreasing and
                    recent_lows.is_monotonic_increasing and
                    df["Close"].iloc[i] > recent_highs.iloc[-1]
                ):
                    matches.append({"pattern": pattern_name, "index": i, "emoji": config["emoji"]})

        elif pattern_name == "Ascending Triangle":
            for i in range(10, len(df)):
                highs = df["High"].iloc[i - 5:i]
                lows = df["Low"].iloc[i - 5:i]
                if (
                    abs(highs.max() - highs.min()) / highs.max() < 0.02 and
                    lows.is_monotonic_increasing
                ):
                    matches.append({"pattern": pattern_name, "index": i, "emoji": config["emoji"]})

        elif pattern_name == "Descending Triangle":
            for i in range(10, len(df)):
                lows = df["Low"].iloc[i - 5:i]
                highs = df["High"].iloc[i - 5:i]
                if (
                    abs(lows.max() - lows.min()) / lows.max() < 0.02 and
                    highs.is_monotonic_decreasing
                ):
                    matches.append({"pattern": pattern_name, "index": i, "emoji": config["emoji"]})

    return matches
