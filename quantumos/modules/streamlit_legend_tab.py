import streamlit as st
from identity_myth_engine import synthesize_identity_myth
from session_indexer import index_session_tags
from ritual_composer import compose_ritual_chain
from belief_drift_animator import plot_belief_drift
from session_orbit import plot_emotional_orbit
from myth_legacy_tracker import read_legacy_log
from animated_identity_plot import plot_identity_evolution

def render_tabbed_dashboard():
    st.set_page_config(layout="wide")
    tabs = st.tabs([
        "🌌 Mythic Identity",
        "📊 Belief Drift",
        "🪐 Emotional Orbit",
        "🪶 Ritual Chain",
        "🏷️ Session Tags",
        "📜 Legacy Tracker"
    ])

    with tabs[0]:
        st.title("🌌 Mythic Identity")
        st.markdown(synthesize_identity_myth())
        st.plotly_chart(plot_identity_evolution())

    with tabs[1]:
        st.title("📊 Belief Drift")
        st.plotly_chart(plot_belief_drift())

    with tabs[2]:
        st.title("🪐 Emotional Orbit")
        st.plotly_chart(plot_emotional_orbit())

    with tabs[3]:
        st.title("🪶 Ritual Chain")
        for stanza in compose_ritual_chain():
            st.code(stanza, language="text")

    with tabs[4]:
        st.title("🏷️ Session Tags")
        for tag in index_session_tags():
            st.markdown(f"- {tag}")

    with tabs[5]:
        st.title("📜 Myth Legacy")
        logs = read_legacy_log()
        for day, entry in logs.items():
            st.markdown(f"**{day}** → {entry}")

render_tabbed_dashboard()
