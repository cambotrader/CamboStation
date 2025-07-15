from signal_overlay import get_recent_signals
def draw_regime_map():
    import streamlit as st
    signals = get_recent_signals()
    for s in signals:
        regime = "Expansion" if s["conviction"] > 0.75 else "Consolidation"
        st.markdown(f"ðŸ•’ {s['timestamp']} | Regime: **{regime}** | Dominant: {s['archetype']} | Tone: {s['mood']} | Conviction Avg: `{round(s['conviction'],2)}`")
