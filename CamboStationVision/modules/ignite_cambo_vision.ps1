# 1. streamlit_memory_tab.py
@"
import streamlit as st
from memory_navigator import list_voice_archives
from ritual_composer import compose_ritual_chain
from identity_myth_engine import synthesize_identity_myth
from session_indexer import index_session_tags
from belief_drift_animator import plot_belief_drift
from myth_orbit_analyzer import analyze_myth_orbit

def render_memory_panel():
    st.title("ðŸ“š CamboStation Memory Stream")
    st.markdown("### ðŸŒŒ Mythic Identity")
    st.markdown(synthesize_identity_myth())
    st.markdown("### ðŸª Emotional Orbit")
    for arc in analyze_myth_orbit():
        st.markdown(arc)
    st.markdown("### ðŸ“Š Belief Drift")
    st.plotly_chart(plot_belief_drift())
    st.markdown("### ðŸª¶ Ritual Chain")
    for stanza in compose_ritual_chain():
        st.code(stanza, language='text')
    st.markdown("### ðŸ·ï¸ Session Tags")
    for tag in index_session_tags():
        st.markdown(f"- {tag}")
    st.markdown("### ðŸ“ Voice Archives")
    logs = list_voice_archives()
    for file, preview in logs:
        st.markdown(f"**{file}**\\n\\n{preview}")
"@ | Set-Content "$HOME\CamboStation_QuantumOS\modules\streamlit_memory_tab.py" -Encoding UTF8

# 2. myth_orbit_analyzer.py
@"
from signal_overlay import get_recent_signals
from collections import defaultdict

def analyze_myth_orbit():
    logs = get_recent_signals()
    archive = defaultdict(list)
    for s in logs:
        tone = "Expansion" if s['conviction'] > 0.75 else "Consolidation"
        arc = f"ðŸª {s['archetype']} drifted through {s['mood']} â†’ {s['signal']} ({tone}) @ {s['conviction']}"
        archive[tone].append(arc)
    output = []
    for regime, lines in archive.items():
        output.append(f"## ðŸ”® Myth Cycle: {regime}")
        output.extend(lines)
    return output
"@ | Set-Content "$HOME\CamboStation_QuantumOS\modules\myth_orbit_analyzer.py" -Encoding UTF8

# 3. Inject "memory suite" mode into cockpit.ps1
(Get-Content "$HOME\CamboStation_QuantumOS\modules\cockpit.ps1") -replace '(\$cmds\s*=\s*@\([^\)]*)', '$1,"memory suite"' | Set-Content "$HOME\CamboStation_QuantumOS\modules\cockpit.ps1"
Add-Content "$HOME\CamboStation_QuantumOS\modules\cockpit.ps1" "`n`"memory suite" { streamlit run `"$HOME\CamboStation_QuantumOS\modules\streamlit_memory_tab.py`" }"

