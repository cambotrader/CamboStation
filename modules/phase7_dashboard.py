import streamlit as st
from signal_memory_replay import replay_signals
from cognitive_simulator import simulate_scenario
from codex_summoner import get_codex_timeline
from personality_grid import evolve_personality

st.title("?? CamboStation Phase 7: Meta Memory + Persona Evolution")

st.subheader("?? Signal Replay")
for s in replay_signals():
    st.markdown(f"- {s}")

st.divider()
st.subheader("?? Simulation Outcome")
for sim in simulate_scenario("Hunter", "aggressive", 47, "BUY"):
    st.markdown(f"- {sim['performance']}")

st.divider()
st.subheader("?? Codex Timeline")
for entry in get_codex_timeline():
    st.markdown(f"- {entry['timestamp']} | Belief: {entry['belief']} | Context: {entry['context']}")

st.divider()
st.subheader("?? Personality State")
state = evolve_personality("win")
for k, v in state.items():
    st.markdown(f"- {k}: **{v}**")
