import streamlit as st
from memory_navigator import list_voice_archives
from ritual_composer import compose_ritual_chain
from identity_myth_engine import synthesize_identity_myth
from session_indexer import index_session_tags
from belief_drift_animator import plot_belief_drift
from myth_orbit_analyzer import analyze_myth_orbit

def render_memory_panel():
    st.title("📚 CamboStation Memory Stream")

    st.markdown("### 🌌 Mythic Identity")
    st.markdown(synthesize_identity_myth())

    st.markdown("### 🪐 Emotional Orbit")
    for arc in analyze_myth_orbit():
        st.markdown(arc)

    st.markdown("### 📊 Belief Drift")
    st.plotly_chart(plot_belief_drift())

    st.markdown("### 🪶 Ritual Chain")
    for stanza in compose_ritual_chain():
        st.code(stanza, language='text')

    st.markdown("### 🏷️ Session Tags")
    for tag in index_session_tags():
        st.markdown(f"- {tag}")

    st.markdown("### 📁 Voice Archives")
    logs = list_voice_archives()
    for file, preview in logs:
        st.markdown(f"**{file}**\n\n{preview}")
render_memory_panel()
