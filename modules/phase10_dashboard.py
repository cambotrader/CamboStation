import streamlit as st
from signal_collider import collide_signals
from strategy_lore import generate_lore
from harmonic_memory import log_harmonic
from myth_conflict_sim import simulate_conflict

st.title("? Phase 10: Harmonic Conflict & Lore Arena")

st.subheader("?? Strategic Lore")
for lore in generate_lore("BUY", "Oracle", "Conviction over chaos"):
    st.markdown(f"- {lore}")

st.divider()
st.subheader("?? Harmonic Memory Log")
for h in log_harmonic("SELL", "reflective", "loss"):
    st.markdown(f"- Signal: {h['signal']} | Emotion: {h['emotion']} | Outcome: {h['outcome']} | Tone: {h['tone']}")

st.divider()
st.subheader("?? Conflict Simulation")
conflict = simulate_conflict("PASS", "BUY")
st.markdown(f"- Ghost: {conflict['ghost']} | Oracle: {conflict['oracle']} ? Verdict: {conflict['verdict']}")

st.divider()
st.subheader("? Signal Collision Result")
collision = collide_signals("BUY", "SELL")
st.markdown(f"- {collision['timestamp']} ? {collision['signalA']} vs {collision['signalB']} = {collision['result']}")
