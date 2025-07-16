legend_archive = []
def synthesize_legend(entry):
    echo = f"?? Echoed Belief: {entry['belief']} under {entry['archetype']} at {entry['timestamp']}"
    legend_archive.append(echo)
    return legend_archive[-3:]
