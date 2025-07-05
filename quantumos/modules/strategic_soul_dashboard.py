import streamlit as st
from global_memory import memory

st.title("?? CamboStation Strategic Soul Dashboard")
st.metric("Archetype", memory["active_archetype"])
st.metric("Mood", memory["recent_trade_mood"])
st.metric("Override Tension", memory["override_tension"])
st.metric("Conviction", f"{memory['conviction_level']:.2f}")
st.write("### Belief Evolution")
st.json(memory["belief_shift"])
