# ðŸ”¥ legend_plus.py
@"
import streamlit as st
from identity_myth_engine import synthesize_identity_myth
from session_indexer import index_session_tags
from ritual_composer import compose_ritual_chain
from belief_drift_animator import plot_belief_drift
from session_orbit import plot_emotional_orbit
from myth_legacy_tracker import read_legacy_log
from animated_identity_plot import plot_identity_evolution
from soulmap_engine import cluster_soulmap
from myth_summarizer import summarize_myth_log

def render_tabbed_dashboard():
    st.set_page_config(layout="wide")
    tabs = st.tabs([
        "ðŸŒŒ Mythic Identity",
        "ðŸ“Š Belief Drift",
        "ðŸª Emotional Orbit",
        "ðŸª¶ Ritual Chain",
        "ðŸ·ï¸ Session Tags",
        "ðŸ“œ Legacy Tracker",
        "ðŸ§­ Soulmap & Closers"
    ])

    with tabs[0]:
        st.title("ðŸŒŒ Mythic Identity")
        st.markdown(synthesize_identity_myth())
        st.plotly_chart(plot_identity_evolution())

    with tabs[1]:
        st.title("ðŸ“Š Belief Drift")
        st.plotly_chart(plot_belief_drift())

    with tabs[2]:
        st.title("ðŸª Emotional Orbit")
        st.plotly_chart(plot_emotional_orbit())

    with tabs[3]:
        st.title("ðŸª¶ Ritual Chain")
        for stanza in compose_ritual_chain():
            st.code(stanza, language="text")

    with tabs[4]:
        st.title("ðŸ·ï¸ Session Tags")
        for tag in index_session_tags():
            st.markdown(f"- {tag}")

    with tabs[5]:
        st.title("ðŸ“œ Myth Legacy")
        logs = read_legacy_log()
        for day, entry in logs.items():
            st.markdown(f"**{day}** â†’ {entry}")

    with tabs[6]:
        st.title("ðŸ§­ Soulmap & Closers")
        st.markdown("### ðŸ”® Archetype-Mood Clusters")
        for line in cluster_soulmap():
            st.markdown(line)
        st.markdown("### ðŸª¶ Poetic Myth Summaries")
        for closer in summarize_myth_log():
            st.markdown(closer)

render_tabbed_dashboard()
"@ | Set-Content "$HOME\CamboStation_QuantumOS\modules\legend_plus.py" -Encoding UTF8

# ðŸ”Š myth_voice_stream.py
@"
from signal_overlay import get_recent_signals
from identity_myth_engine import synthesize_identity_myth

def narrate_voice_stream():
    logs = get_recent_signals()
    stream = []
    for s in logs:
        tone = "expanding" if s['conviction'] > 0.75 else "contracting"
        line = f"ðŸŽ™ï¸ CamboStation spoke as '{s['archetype']}', in a mood of '{s['mood']}', while {tone} toward '{s['signal']}' @ {s['conviction']:.2f}"
        stream.append(line)
    print(synthesize_identity_myth())
    for line in stream:
        print(line)
"@ | Set-Content "$HOME\CamboStation_QuantumOS\modules\myth_voice_stream.py" -Encoding UTF8

# âž• Add modes to cockpit.ps1
(Get-Content "$HOME\CamboStation_QuantumOS\modules\cockpit.ps1") -replace '(\$cmds\s*=\s*@\([^\)]*)', '$1,"legend plus","voice stream"' | Set-Content "$HOME\CamboStation_QuantumOS\modules\cockpit.ps1"

Add-Content "$HOME\CamboStation_QuantumOS\modules\cockpit.ps1" "`n`"legend plus" { streamlit run `"$base\legend_plus.py`" }"
Add-Content "$HOME\CamboStation_QuantumOS\modules\cockpit.ps1" "`n`"voice stream" { python `"$base\myth_voice_stream.py`" }"
