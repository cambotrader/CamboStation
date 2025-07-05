import plotly.graph_objs as go
from signal_overlay import get_recent_signals

def plot_belief_drift():
    logs = get_recent_signals()
    x = list(range(len(logs)))
    y_conviction = [s['conviction'] for s in logs]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y_conviction, mode='lines+markers', name='Conviction'))
    fig.update_layout(title='Belief Drift vs Conviction', xaxis_title='Signal #', yaxis_title='Conviction')
    return fig
