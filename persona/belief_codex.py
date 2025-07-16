# belief_codex.py — Cognitive and Emotional Imprint Registry

class BeliefCodex:
    def __init__(self):
        self.values = {}
        self.emotional_weights = {}

    def encode_belief(self, key, value, emotion='neutral'):
        self.values[key] = value
        self.emotional_weights[key] = emotion

    def retrieve(self, key):
        return {
            'value': self.values.get(key),
            'emotion': self.emotional_weights.get(key)
        }
