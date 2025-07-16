# ðŸŽ¼ harmonics_panel.py
@"
import streamlit as st
from tone_tracer import trace_tone_curve
from soulmap_engine import cluster_soulmap
from myth_summarizer import summarize_myth_log

def render_harmonics_panel():
    st.set_page_config(layout="wide")
    st.title("ðŸŽ¼ CamboStation Harmonics Panel")
    
    st.markdown("### ðŸŽµ Tone Curve")
    for line in trace_tone_curve():
        st.markdown(f"- {line}")
    
    st.markdown("### ðŸ”® Constellation Clusters")
    for cluster in cluster_soulmap():
        st.markdown(cluster)

    st.markdown("### ðŸ“œ Poetic Closers")
    for closer in summarize_myth_log():
        st.markdown(closer)
"@ | Set-Content "$HOME\CamboStation_QuantumOS\modules\harmonics_panel.py" -Encoding UTF8

# ðŸª¶ ritual_tab.py
@"
import streamlit as st
from ritual_journal import add_poetic_reflection, read_journal

def render_ritual_tab():
    st.set_page_config(layout="wide")
    st.title("ðŸª¶ Ritual Journal")

    st.markdown("### Add Poetic Reflection")
    user_input = st.text_area("Compose your myth reflection")
    if st.button("Add to Ritual Log") and user_input:
        add_poetic_reflection(user_input)
        st.success("Reflection added!")

    st.markdown("### ðŸ“œ Past Reflections")
    journal = read_journal()
    for day, note in journal.items():
        st.markdown(f"**{day}** â†’ {note}")
"@ | Set-Content "$HOME\CamboStation_QuantumOS\modules\ritual_tab.py" -Encoding UTF8

# âž• Wire cockpit modes 16 + 17
(Get-Content "$HOME\CamboStation_QuantumOS\modules\cockpit.ps1") -replace '(\$cmds\s*=\s*@\([^\)]*)', '$1,"harmonics panel","ritual tab"' | Set-Content "$HOME\CamboStation_QuantumOS\modules\cockpit.ps1"

Add-Content "$HOME\CamboStation_QuantumOS\modules\cockpit.ps1" "`n`"harmonics panel" { streamlit run `"$base\harmonics_panel.py`" }"
Add-Content "$HOME\CamboStation_QuantumOS\modules\cockpit.ps1" "`n`"ritual tab" { streamlit run `"$base\ritual_tab.py`" }"
