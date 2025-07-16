import streamlit as st
from dimensional_signal_mapper import last_signals
from regime_overlay import recent_snapshots
from persona_volatility_tracker import recent_volatility

st.title("?? Multiverse Signal Theatre")

st.subheader("?? Signal Arena")
for s in last_signals():
    st.markdown(f"- {s['timestamp']} | Signal: {s['signal']} | Archetype: {s['archetype']} | Mood: {s['mood']} | VIX: {s['volatility']}")

st.divider()
st.subheader("?? Regime Overlays")
for r in recent_snapshots():
    st.markdown(f"- {r['timestamp']} | Persona: {r['persona']} | Mood: {r['mood']} | Sentiment: {r['sentiment']} | Volume: {r['volume']}")

st.divider()
st.subheader("?? Archetype Volatility Log")
for v in recent_volatility():
    st.markdown(f"- {v['timestamp']} | {v['archetype']} | ?VIX: {v['delta']} | Outcome: {v['outcome']}")
