import streamlit as st
import json, os

from modules import voting_system, pattern_engine, sentiment_grid, execution_agent

def load_manifest():
    manifest_path = os.path.join(os.path.dirname(__file__), "..", "config", "modules.manifest.json")
    try:
        with open(manifest_path, "r", encoding="utf-8-sig") as f:
            return json.load(f)
    except:
        return {}

def dispatch_modules(selected_asset):
    manifest = load_manifest()

    # Dispatch Voting System if toggled
    if manifest.get("features", {}).get("voting_system", False):
        st.markdown("### 🗳 AI Voting Consensus")
        signal = render_voting(selected_asset)
        if signal["majority"] in ["buy", "sell"] and signal["confidence"] >= 0.75:
            st.markdown("### 🎯 Signal Routed to Execution Agent")
            execution_agent.render(signal["majority"], signal["confidence"])

    # Dispatch Pattern + Sentiment (example)
    if manifest.get("features", {}).get("pattern_engine", False):
        pattern_engine.render()
    if manifest.get("features", {}).get("sentiment_grid", False):
        sentiment_grid.render()

def render_voting(asset):
    engine_signals = {
        "stocks": {
            "grok": {"signal": "buy", "confidence": 0.82},
            "chatgpt": {"signal": "buy", "confidence": 0.74}
        },
        "crypto": {
            "gemini": {"signal": "sell", "confidence": 0.81},
            "chatgpt": {"signal": "neutral", "confidence": 0.65}
        },
        "options": {
            "tradegpt": {"signal": "buy", "confidence": 0.79},
            "grok": {"signal": "neutral", "confidence": 0.52}
        }
    }

    signals = engine_signals.get(asset.lower(), {})
    if not signals:
        st.warning("No signals defined for this asset class.")
        return {"majority": "neutral", "confidence": 0.0}

    vote_count = {}
    total_conf = 0
    for engine, vote in signals.items():
        signal = vote["signal"]
        conf = vote["confidence"]
        vote_count[signal] = vote_count.get(signal, 0) + 1
        total_conf += conf

    majority = max(vote_count, key=vote_count.get)
    avg_conf = round(total_conf / len(signals), 2)

    st.markdown(f"**Majority Signal:** `{majority.upper()}`")
    st.markdown(f"**Average Confidence:** `{avg_conf}`")

    return {"majority": majority, "confidence": avg_conf}
