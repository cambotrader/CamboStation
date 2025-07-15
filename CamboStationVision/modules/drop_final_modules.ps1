from pathlib import Path
import json, os

# 1. memory_navigator.py
memory_navigator = """
import os

def list_voice_archives(folder='.', filter_by=None):
    logs = []
    for file in os.listdir(folder):
        if file.startswith("voice_archive_") and file.endswith(".txt"):
            path = os.path.join(folder, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            if filter_by:
                if filter_by.lower() not in content.lower():
                    continue
            logs.append((file, content[:500] + '...'))
    return logs
"""
Path("memory_navigator.py").write_text(memory_navigator, encoding="utf-8")

# 2. belief_drift_animator.py
belief_drift = """
import plotly.graph_objs as go
from signal_overlay import get_recent_signals

def plot_belief_drift():
    logs = get_recent_signals()
    x = list(range(len(logs)))
    y_conviction = [s['conviction'] for s in logs]
    y_drift = [s['mood'] for s in logs]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y_conviction, mode='lines+markers', name='Conviction'))
    fig.update_layout(title='Belief Drift vs Conviction', xaxis_title='Signal #', yaxis_title='Conviction')
    return fig
"""
Path("belief_drift_animator.py").write_text(belief_drift, encoding="utf-8")

# 3. ritual_composer.py
ritual_composer = """
import glob

def compose_ritual_chain():
    files = sorted(glob.glob("voice_archive_*.txt"))
    chain = []
    for f in files:
        with open(f, "r", encoding="utf-8") as file:
            content = file.read()
            lines = [line for line in content.splitlines() if "🪶" in line or "Thus" in line]
            if lines:
                chain.append("\\n".join(lines))
    return chain
"""
Path("ritual_composer.py").write_text(ritual_composer, encoding="utf-8")

# 4. identity_myth_engine.py
identity_myth = """
from signal_overlay import get_recent_signals
from collections import Counter

def synthesize_identity_myth():
    logs = get_recent_signals()
    archetypes = [s['archetype'] for s in logs]
    moods = [s['mood'] for s in logs]
    dominant_archetype = Counter(archetypes).most_common(1)[0]
    dominant_mood = Counter(moods).most_common(1)[0]
    return f"🌌 CamboStation speaks most often as '{dominant_archetype[0]}' in a mood of '{dominant_mood[0]}'"
"""
Path("identity_myth_engine.py").write_text(identity_myth, encoding="utf-8")

# 5. session_indexer.py
session_indexer = """
from signal_overlay import get_recent_signals

def index_session_tags():
    logs = get_recent_signals()
    tags = []
    for s in logs:
        regime = "Expansion" if s['conviction'] > 0.75 else "Consolidation"
        tags.append(f"[{regime}] {s['archetype']} | {s['mood']} | {s['signal']}")
    return tags
"""
Path("session_indexer.py").write_text(session_indexer, encoding="utf-8")
