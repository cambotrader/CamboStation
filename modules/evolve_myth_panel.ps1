# ðŸŸª streamlit_legend_tab.py
@"
import streamlit as st
from identity_myth_engine import synthesize_identity_myth
from session_indexer import index_session_tags
from ritual_composer import compose_ritual_chain
from belief_drift_animator import plot_belief_drift
from session_orbit import plot_emotional_orbit
from myth_legacy_tracker import read_legacy_log
from animated_identity_plot import plot_identity_evolution

def render_tabbed_dashboard():
    st.set_page_config(layout="wide")
    tabs = st.tabs(["ðŸŒŒ Mythic Identity", "ðŸ“Š Belief Drift", "ðŸª Emotional Orbit", "ðŸª¶ Ritual Chain", "ðŸ“ Session Tags", "ðŸ“œ Legacy Tracker"])

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
        st.title("ðŸ“ Session Tags")
        for tag in index_session_tags():
            st.markdown(f"- {tag}")

    with tabs[5]:
        st.title("ðŸ“œ Myth Legacy")
        logs = read_legacy_log()
        for day, entry in logs.items():
            st.markdown(f"**{day}** â†’ {entry}")
            
render_tabbed_dashboard()
"@ | Set-Content "$HOME\CamboStation_QuantumOS\modules\streamlit_legend_tab.py" -Encoding UTF8

# ðŸŸ¦ animated_identity_plot.py
@"
from datetime import datetime
import json, os
import plotly.graph_objs as go

def plot_identity_evolution():
    log_path = "$HOME\\CamboStation_QuantumOS\\modules\\myth_legacy.json"
    if not os.path.exists(log_path): return go.Figure()

    with open(log_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    dates = list(data.keys())
    moods = [entry.split("'")[-2] for entry in data.values()]
    fig = go.Figure(go.Scatter(x=dates, y=moods, mode="lines+markers"))
    fig.update_layout(title="ðŸŒŒ Identity Mood Over Time", xaxis_title="Date", yaxis_title="Mood")
    return fig
"@ | Set-Content "$HOME\CamboStation_QuantumOS\modules\animated_identity_plot.py" -Encoding UTF8

# ðŸŸ¨ myth_legacy_tracker.py
@"
import json
from identity_myth_engine import synthesize_identity_myth
from datetime import datetime

def log_myth_today():
    entry = synthesize_identity_myth()
    path = "$HOME\\CamboStation_QuantumOS\\modules\\myth_legacy.json"
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except:
        data = {}

    today = datetime.today().strftime("%Y-%m-%d")
    data[today] = entry
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def read_legacy_log():
    path = "$HOME\\CamboStation_QuantumOS\\modules\\myth_legacy.json"
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}
"@ | Set-Content "$HOME\CamboStation_QuantumOS\modules\myth_legacy_tracker.py" -Encoding UTF8

# ðŸŸ§ Add "legend panel" to cockpit.ps1
(Get-Content "$HOME\CamboStation_QuantumOS\modules\cockpit.ps1") -replace '(\$cmds\s*=\s*@\([^\)]*)', '$1,"legend panel"' | Set-Content "$HOME\CamboStation_QuantumOS\modules\cockpit.ps1"
Add-Content "$HOME\CamboStation_QuantumOS\modules\cockpit.ps1" "`n`"legend panel" { streamlit run `"$HOME\CamboStation_QuantumOS\modules\streamlit_legend_tab.py`" }"
