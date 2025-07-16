# execution_playlist.py — Signal Sequencer

class ExecutionPlaylist:
    def __init__(self):
        self.signals = []

    def queue_signal(self, signal):
        print(f"Queued signal: {signal}")
        self.signals.append(signal)

    def execute_signals(self):
        print("Executing all queued signals:")
        while self.signals:
            signal = self.signals.pop(0)
            print(f"→ Executing: {signal}")
