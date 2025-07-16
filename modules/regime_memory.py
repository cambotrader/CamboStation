regime_log = []
def log_regime(mood, archetype, volatility):
    regime_log.append({"mood": mood, "archetype": archetype, "volatility": volatility})
def get_past_regimes(): return regime_log[-5:]
