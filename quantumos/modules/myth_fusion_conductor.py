def fuse_archetypes(a, b):
    fusion_map = {
        ("Ghost","Hunter"): "Silent Precision",
        ("Oracle","Trickster"): "Ambiguous Insight",
        ("Prophet","Contrarian"): "Chaotic Vision"
    }
    return fusion_map.get((a, b), f"{a}-{b} Fusion")
