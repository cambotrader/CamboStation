import os
import streamlit as st
from signal_overlay import get_recent_signals
from regime_map import draw_regime_map

reload_flag = os.path.join(os.path.expanduser("~"), "CamboStation_QuantumOS", "modules", ".reload_flag")
def check_reload():
    try:
        with open(reload_flag, "r", encoding="utf-8") as f:
            return f.read().strip()
    except:
        return "ready"

if check_reload() == "reload":
    st.toast("🔁 Reload flag detected — cockpit logic refreshed.")

def simulate_tone_drift():
    mood_counts = {}
    for s in get_recent_signals():
        mood = s["mood"]
        mood_counts[mood] = mood_counts.get(mood, 0) + 1
    total = sum(mood_counts.values())
    return {m: round(c/total, 2) for m, c in mood_counts.items()}

tabs = st.tabs([
    "🎙️ Mission Feed",
    "📊 Signal History",
    "📡 Regime Map Grid",
    "🌫️ Tone Drift Analyzer"
])

with tabs[0]:
    st.title("🎙️ Mission Feed")
    st.markdown("- Archetype: **Oracle**")
    st.markdown("- Signal: `BUY` | Conviction: 0.79")
    st.markdown("- Mood: `Focused`")
    st.markdown("- Belief: \"Bias reveals divergence\"")

with tabs[1]:
    st.title("📊 Signal History")
    for log in get_recent_signals():
        st.markdown(f"- {log['timestamp']} | Signal: **{log['signal']}** | Archetype: {log['archetype']} | Mood: {log['mood']} | Conviction: {log['conviction']}")

with tabs[2]:
    st.title("📡 Strategic Regime Map")
    draw_regime_map()

with tabs[3]:
    st.title("🌫️ Tone Drift Analyzer")
    drift = simulate_tone_drift()
    for mood, pct in drift.items():
        st.markdown(f"- Mood: **{mood}** → Drift Weight: `{pct}`")
