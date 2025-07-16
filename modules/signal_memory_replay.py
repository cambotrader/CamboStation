signal_journal = []
def record_signal(entry):
    signal_journal.append(entry)
def replay_signals(n=5):
    return signal_journal[-n:]
