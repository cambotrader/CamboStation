def harmonize_codex(belief_entries):
    themes = set([b["theme"] for b in belief_entries])
    core_thread = "• ".join(sorted(themes))
    return f"OmniCodex Themes: {core_thread}"
