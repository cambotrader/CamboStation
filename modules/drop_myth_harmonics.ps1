# ðŸ§µ tone_tracer.py
@"
import json
from datetime import datetime

def trace_tone_curve():
    path = "$HOME\\CamboStation_QuantumOS\\modules\\myth_legacy.json"
    try:
        with open(path, "r", encoding="utf-8") as f:
            logs = json.load(f)
    except:
        return []

    curve = []
    for date, entry in logs.items():
        mood = entry.split("'")[-2]
        curve.append(f"{date}: {mood}")
    return curve
"@ | Set-Content "$HOME\CamboStation_QuantumOS\modules\tone_tracer.py" -Encoding UTF8

# ðŸŽ§ voice_panel.py
@"
import streamlit as st
from myth_voice_stream import narrate_voice_stream

def render_voice_panel():
    st.title("ðŸŽ§ CamboStation Voice Stream")
    st.markdown("Real-time narration of identity, mood, and conviction.")
    st.code(narrate_voice_stream(), language="text")
"@ | Set-Content "$HOME\CamboStation_QuantumOS\modules\voice_panel.py" -Encoding UTF8

# ðŸ“œ ritual_journal.py
@"
import json
from datetime import datetime

def add_poetic_reflection(text):
    path = "$HOME\\CamboStation_QuantumOS\\modules\\ritual_log.json"
    try:
        with open(path, "r", encoding="utf-8") as f:
            journal = json.load(f)
    except:
        journal = {}

    today = datetime.today().strftime("%Y-%m-%d")
    journal[today] = text
    with open(path, "w", encoding="utf-8") as f:
        json.dump(journal, f, indent=2, ensure_ascii=False)

def read_journal():
    path = "$HOME\\CamboStation_QuantumOS\\modules\\ritual_log.json"
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}
"@ | Set-Content "$HOME\CamboStation_QuantumOS\modules\ritual_journal.py" -Encoding UTF8

# ðŸŽ¼ myth_harmonics.py
@"
from tone_tracer import trace_tone_curve
from soulmap_engine import cluster_soulmap
from myth_summarizer import summarize_myth_log

def detect_myth_rhythm():
    tones = trace_tone_curve()
    clusters = cluster_soulmap()
    closers = summarize_myth_log()

    output = []
    output.append("ðŸŽ¼ Tone Curve:")
    output.extend(tones)
    output.append("\\nðŸ”® Constellation Clusters:")
    output.extend(clusters)
    output.append("\\nðŸ“œ Poetic Closers:")
    output.extend(closers)
    return "\\n".join(output)
"@ | Set-Content "$HOME\CamboStation_QuantumOS\modules\myth_harmonics.py" -Encoding UTF8
