montage_log = []
def compose_montage(signals):
    clip = f"Montage of conviction: {', '.join(signals)}"
    montage_log.append(clip)
    return montage_log[-3:]
