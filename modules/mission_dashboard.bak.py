import streamlit as st
from signal_overlay import get_recent_signals
from vote_grid import get_votes
from codex_visualizer import get_codex_state

narrative_state = {
    "voice": "Reflective Strategist",
    "structure": "Belief → Mood → Action",
    "tone": "Cautious Introspection"
}

tabs = st.tabs([
    "🎙️ Mission Feed",
    "🧠 Strategy Tone",
    "📊 Signal History Overlay",
    "🔁 Archetype Voting Grid",
    "🧿 Codex Resonance Visualizer"
])

with tabs[0]:
    st.title("🎙️ Live Strategic Feed")
    st.markdown("- Archetype: **Oracle**")
    st.markdown("- Mission: “Hold signal until divergence clarified.”")
    st.markdown("- Mood: Reflective → Cautious")
    st.markdown("- Signal Status: `PASS`")
    st.markdown("- Codex Belief: “Restraint signals depth, not delay.”")

with tabs[1]:
    st.title("🧠 Voice Signature")
    st.markdown(f"- Style: **{narrative_state['voice']}**")
    st.markdown(f"- Tone: **{narrative_state['tone']}**")
    st.markdown(f"- Structure: `{narrative_state['structure']}`")

with tabs[2]:
    st.title("📊 Signal History Overlay")
    for log in get_recent_signals():
        st.markdown(
            f"- {log['timestamp']} | Signal: **{log['signal']}** | Mood: {log['mood']} | Archetype: {log['archetype']} | Conviction: {log['conviction']}"
        )

with tabs[3]:
    st.title("🔁 Archetype Voting Grid")
    votes = get_votes()
    for agent, data in votes.items():
        st.markdown(f"- {agent}: `{data['vote']}` | Tension Index: `{data['tension']}`")

with tabs[4]:
    st.title("🧿 Codex Resonance Visualizer")
    codex = get_codex_state()
    for belief, data in codex.items():
        st.markdown(
            f"- “{belief}” → Resonance: `{data['resonance']}` | Mutation Risk: `{data['mutation_risk']}`"
        )
