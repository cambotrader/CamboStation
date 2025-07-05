from signal_overlay import get_recent_signals
import plotly.graph_objs as go

def plot_emotional_orbit():
    logs = get_recent_signals()
    archetypes = [s['archetype'] for s in logs]
    moods = [s['mood'] for s in logs]
    conviction = [s['conviction'] for s in logs]
    colors = ["blue" if c > 0.75 else "gray" for c in conviction]

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=archetypes,
        y=moods,
        mode="markers+text",
        marker=dict(color=colors, size=10),
        text=[f"{s['signal']} ({s['conviction']})" for s in logs],
        textposition="top center"
    ))

    fig.update_layout(
        title="🪐 Emotional Orbit of Sessions",
        xaxis_title="Archetype",
        yaxis_title="Mood"
    )
    return fig
