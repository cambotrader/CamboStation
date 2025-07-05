from signal_overlay import get_recent_signals
import pandas as pd
import streamlit as st

def render_belief_grid():
    signals = get_recent_signals()
    data = [{"Mood": s["mood"], "Conviction": s["conviction"], "Archetype": s["archetype"]} for s in signals]
    df = pd.DataFrame(data)
    st.title("🧩 Conviction vs Tone Drift Grid")
    st.scatter_chart(df, x="Conviction", y="Mood", color="Archetype")
