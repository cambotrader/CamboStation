import streamlit as st
from modules import trade_log, execution_delay, risk_filter, live_alerts

def render(signal="neutral", confidence=0.0, asset="unspecified"):
    st.subheader("🎯 Execution Agent")

    # Send alert
    live_alerts.alert(signal, confidence)

    # Apply risk filter
    if not risk_filter.apply_filter(mock_vix=32.1):
        trade_log.log_trade(asset, signal, confidence, "blocked_by_risk")
        return

    # Apply execution delay
    execution_delay.apply_delay(3)

    # Final routing based on signal strength
    if signal.lower() in ["buy", "sell"]:
        st.markdown(f"**Received Signal:** `{signal.upper()}` with confidence `{confidence}`")
        if confidence >= 0.85:
            outcome = "full_trade"
            st.success("✅ Executing full-size trade setup.")
            st.info("💡 Confidence high — confirmed entry.")
        elif confidence >= 0.70:
            outcome = "partial_trade"
            st.success("⚠️ Executing partial-size trade.")
        else:
            outcome = "suppressed_trade"
            st.warning("🧐 Confidence low — trade suppressed.")
    else:
        outcome = "neutral_vote"
        st.info("No actionable signal detected.")

    # Log execution
    trade_log.log_trade(asset, signal, confidence, outcome)
