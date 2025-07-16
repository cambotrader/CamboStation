from datetime import datetime
import json, os
import plotly.graph_objs as go

def plot_identity_evolution():
    log_path = os.path.expandvars("$HOME\\CamboStation_QuantumOS\\modules\\myth_legacy.json")
    if not os.path.exists(log_path):
        return go.Figure()

    with open(log_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    dates = list(data.keys())
    moods = [entry.split("'")[-2] for entry in data.values()]

    fig = go.Figure(go.Scatter(x=dates, y=moods, mode="lines+markers"))
    fig.update_layout(
        title="🌌 Identity Mood Over Time",
        xaxis_title="Date",
        yaxis_title="Mood"
    )
    return fig
