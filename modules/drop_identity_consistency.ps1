# ðŸ“ˆ identity_consistency_panel.py
@"
import streamlit as st
from identity_drift_analyzer import analyze_identity_drift
from myth_index_score import compute_myth_index
import matplotlib.pyplot as plt
import json
import os

def render_consistency_panel():
    st.set_page_config(layout="wide")
    st.title("ðŸ“ˆ Identity Consistency Dashboard")

    # Mood Volatility Chart
    path = os.path.expandvars("$HOME\\CamboStation_QuantumOS\\modules\\myth_legacy.json")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            logs = json.load(f)

        dates = sorted(logs.keys())
        moods = [logs[d].split("'")[-2] for d in dates]
        mood_set = sorted(set(moods))
        mood_map = {m: i for i, m in enumerate(mood_set)}
        mood_vals = [mood_map[m] for m in moods]

        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(dates, mood_vals, marker='o', color='blue')
        ax.set_title("ðŸª Mood Volatility")
        ax.set_xticklabels(dates, rotation=45)
        ax.set_yticks(list(mood_map.values()))
        ax.set_yticklabels(list(mood_map.keys()))
        st.pyplot(fig)

    # Weekly Drift Clusters
    st.markdown("### ðŸ”® Weekly Archetype-Mood Clusters")
    for line in analyze_identity_drift():
        st.markdown(line)

    # Index Score Interpretation
    st.markdown("### ðŸ“Š Myth Index Score")
    st.code(compute_myth_index(), language="text")

render_consistency_panel()
"@ | Set-Content "$HOME\CamboStation_QuantumOS\modules\identity_consistency_panel.py" -Encoding UTF8

# Wire cockpit mode 22 + 23 + 24
$cockpit = "$HOME\CamboStation_QuantumOS\modules\cockpit.ps1"
$content = Get-Content $cockpit -Raw

if ($content -notmatch '"mood chart"') {
    $content = $content -replace '(\$cmds\s*=\s*@\([^\)]*)', '$1,"mood chart","drift analyzer","consistency panel"'
    $content += "`n    `"mood chart`" { python `"$base\myth_index_plot.py`" }"
    $content += "`n    `"drift analyzer`" { python `"$base\identity_drift_analyzer.py`" }"
    $content += "`n    `"consistency panel`" { streamlit run `"$base\identity_consistency_panel.py`" }"
    Set-Content $cockpit -Value $content -Encoding UTF8
    Write-Host "âœ… Modes 22â€“24 added."
} else {
    Write-Host "âœ… Modes already wired."
}
