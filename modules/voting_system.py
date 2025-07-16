import streamlit as st

def render():
    st.subheader("🗳 AI Voting System")

    # Simulated signal input from engines
    signal_votes = {
        "grok": {"signal": "buy", "confidence": 0.85},
        "tradegpt": {"signal": "buy", "confidence": 0.77},
        "chatgpt": {"signal": "neutral", "confidence": 0.50},
        "gemini": {"signal": "buy", "confidence": 0.90}
    }

    # Count votes and confidence
    vote_count = {}
    total_conf = 0
    for engine, vote in signal_votes.items():
        signal = vote["signal"]
        conf = vote["confidence"]
        vote_count[signal] = vote_count.get(signal, 0) + 1
        total_conf += conf

    majority = max(vote_count, key=vote_count.get)
    avg_conf = round(total_conf / len(signal_votes), 2)
    strength = "HIGH" if avg_conf > 0.75 else "MEDIUM" if avg_conf > 0.5 else "LOW"

    st.markdown(f"**Majority Signal:** `{majority.upper()}`")
    st.markdown(f"**Average Confidence:** `{avg_conf}`")
    st.markdown(f"**Consensus Strength:** `{strength}`")

    st.info("This consensus module computes dominant signal bias from AI engines. Ready for future integration with asset-specific execution.")
