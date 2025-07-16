import streamlit as st
from persona_hierarchy import determine_priority
from strategy_feedback_loop import reinforce_agent_beliefs

st.title("?? Mythic Agent Swarm Dashboard")

st.subheader("?? Agent Priority")
agents = [
    {"name":"Ghost","conviction":0.84,"accuracy":0.76},
    {"name":"Oracle","conviction":0.78,"accuracy":0.83},
    {"name":"Trickster","conviction":0.66,"accuracy":0.52}
]
priority = determine_priority(agents)
for p in priority:
    st.markdown(f"- {p}")

st.divider()
st.subheader("?? Belief Feedback")
for b in reinforce_agent_beliefs("Oracle", "win"):
    st.markdown(f"- {b}")
