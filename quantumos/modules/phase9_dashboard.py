import streamlit as st
from execution_playlist import add_to_playlist
from strategy_montage import compose_montage
from conviction_harmonics import calculate_harmonics
from belief_broadcast import broadcast_belief

st.title("?? Phase 9: Strategic Myth Orchestration")

st.subheader("?? Execution Playlist")
for p in add_to_playlist("BUY", "Conviction before noise", "Focused"):
    st.markdown(f"- {p['timestamp']} | {p['signal']} | {p['belief']} | {p['mood']}")

st.divider()
st.subheader("?? Strategy Montage")
montage = compose_montage(["BUY", "PASS", "SELL"])
for m in montage:
    st.markdown(f"- {m}")

st.divider()
st.subheader("?? Conviction Harmonics")
harm = calculate_harmonics([0.82, 0.91, 0.76])
st.markdown(f"- Tone: **{harm['tone']}** | Avg Strength: **{harm['average']}**")

st.divider()
st.subheader("?? Belief Broadcast")
msg = broadcast_belief("BUY", harm["tone"], "Oracle")
st.markdown(f"- {msg}")
