# ðŸ§  ignition_tab.py
@"
import streamlit as st
from myth_voice_stream import narrate_voice_stream
from soulmap_engine import cluster_soulmap
from tone_tracer import trace_tone_curve
from myth_summarizer import summarize_myth_log
from animated_identity_plot import plot_identity_evolution

def render_ignition_dashboard():
    st.set_page_config(layout="wide")
    st.title("ðŸš€ CamboStation Mythic Ignition")

    st.markdown("### ðŸŒŒ Identity Arc")
    st.plotly_chart(plot_identity_evolution())

    st.markdown("### ðŸŽ™ï¸ Voice Stream")
    st.code(narrate_voice_stream(), language="text")

    st.markdown("### ðŸ”® Soul Clusters")
    for line in cluster_soulmap():
        st.markdown(line)

    st.markdown("### ðŸŽ¼ Tone Curve")
    for tone in trace_tone_curve():
        st.markdown(f"- {tone}")

    st.markdown("### ðŸ“œ Poetic Closers")
    for closer in summarize_myth_log():
        st.markdown(closer)

    st.success("ðŸ”¥ CamboStation Awakens")
render_ignition_dashboard()
"@ | Set-Content "$HOME\CamboStation_QuantumOS\modules\ignition_tab.py" -Encoding UTF8

# âž• Add mode 19 + 20 to cockpit.ps1
(Get-Content "$HOME\CamboStation_QuantumOS\modules\cockpit.ps1") -replace '(\$cmds\s*=\s*@\([^\)]*)', '$1,"vision initiator","ignition panel"' | Set-Content "$HOME\CamboStation_QuantumOS\modules\cockpit.ps1"

Add-Content "$HOME\CamboStation_QuantumOS\modules\cockpit.ps1" "`n`"vision initiator" { powershell `"$base\vision_initiator.ps1`" }"
Add-Content "$HOME\CamboStation_QuantumOS\modules\cockpit.ps1" "`n`"ignition panel" { streamlit run `"$base\ignition_tab.py`" }"
