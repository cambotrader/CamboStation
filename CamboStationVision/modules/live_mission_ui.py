import streamlit as st

narrative_state = {
    "voice": "Reflective Strategist",
    "structure": "Belief → Mood → Action",
    "tone": "Cautious Introspection"
}

tab1, tab2 = st.tabs(["🎙️ Mission Feed", "🧠 Strategy Tone"])

with tab1:
    st.title("Live Strategic Feed")
    st.markdown("- **Archetype**: `Oracle`")
    st.markdown("- **Mission**: “Hold signal until divergence clarified.”")
    st.markdown("- **Mood**: Reflective → Cautious")
    st.markdown("- **Signal Status**: `PASS`")
    st.markdown("- **Codex Belief**: “Restraint signals depth, not delay.”")

with tab2:
    st.title("Voice Signature")
    st.markdown(f"- Voice Style: **{narrative_state['voice']}**")
    st.markdown(f"- Tone: **{narrative_state['tone']}**")
    st.markdown(f"- Structure: `{narrative_state['structure']}`")
    st.markdown("🧠 Broadcast Mode: Strategic Myth Composer")
