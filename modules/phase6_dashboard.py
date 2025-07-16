import streamlit as st
from archetype_drift import simulate_drift
from belief_reinforcer import reinforcement_log
from strategy_publisher import publish_strategy

st.title("?? Sovereign Sync Terminal")
st.subheader("?? Belief Reinforcements")
for r in reinforcement_log: st.markdown(f"- {r}")

st.divider()
st.subheader("?? Archetype Drift")
for d in simulate_drift("Ghost", {"preferred":"Oracle", "vix":45, "mood":"reflective"}):
    st.markdown(f"- Drift: {d['from']} ? {d['to']} | VIX: {d['volatility']} | Tone: {d['tone']} | {d['timestamp']}")

st.divider()
st.subheader("??? Strategy Broadcast")
msg = publish_strategy("BUY", "Cautious Clarity", "Oracle", "Conviction before precision")
st.markdown(f"- {msg}")
