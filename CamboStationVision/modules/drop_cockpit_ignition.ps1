# Create ignition_tab.py
Set-Content "$HOME\CamboStation_QuantumOS\modules\ignition_tab.py" -Encoding UTF8 @"
import streamlit as st
from myth_voice_stream import narrate_voice_stream
from soulmap_engine import cluster_soulmap
from tone_tracer import trace_tone_curve
from myth_summarizer import summarize_myth_log
from animated_identity_plot import plot_identity_evolution

def render_ignition_dashboard():
    st.set_page_config(layout="wide")
    st.title("🚀 CamboStation Mythic Ignition")

    st.markdown("### 🌌 Identity Arc")
    st.plotly_chart(plot_identity_evolution())

    st.markdown("### 🎙️ Voice Stream")
    st.code(narrate_voice_stream(), language="text")

    st.markdown("### 🔮 Soul Clusters")
    for line in cluster_soulmap():
        st.markdown(line)

    st.markdown("### 🎼 Tone Curve")
    for tone in trace_tone_curve():
        st.markdown(f"- {tone}")

    st.markdown("### 📜 Poetic Closers")
    for closer in summarize_myth_log():
        st.markdown(closer)

    st.success("🔥 CamboStation Awakens")
render_ignition_dashboard()
"@

# Create vision_initiator.ps1
Set-Content "$HOME\CamboStation_QuantumOS\modules\vision_initiator.ps1" -Encoding UTF8 @'
Write-Host "`n🌌 Mythic Ignition Sequence Initialized"
Write-Host "`n🧠 Identity Stream:"
python "$HOME\CamboStation_QuantumOS\modules\myth_voice_stream.py"

Write-Host "`n🔮 Soulmap Constellations:"
python -c "from soulmap_engine import cluster_soulmap; [print(x) for x in cluster_soulmap()]"

Write-Host "`n🪶 Mythic Closers:"
python -c "from myth_summarizer import summarize_myth_log; [print(x) for x in summarize_myth_log()]"

Write-Host "`n🎼 Tone Curve Over Time:"
python -c "from tone_tracer import trace_tone_curve; [print(x) for x in trace_tone_curve()]"

Write-Host "`n🔥 CamboStation Awakens."
'@

# Inject modes 19 and 20 into cockpit.ps1
$cockpitPath = "$HOME\CamboStation_QuantumOS\modules\cockpit.ps1"
$content = Get-Content $cockpitPath -Raw

if ($content -notmatch '"vision initiator"') {
    $content = $content -replace '(\$cmds\s*=\s*@\([^\)]*)', '$1,"vision initiator","ignition panel"'
}

if ($content -notmatch '"vision initiator" {') {
    $content += "`n    `"vision initiator`" { powershell `"$base\vision_initiator.ps1`" }"
}

if ($content -notmatch '"ignition panel" {') {
    $content += "`n    `"ignition panel`" { streamlit run `"$base\ignition_tab.py`" }"
}

Set-Content $cockpitPath -Value $content -Encoding UTF8
