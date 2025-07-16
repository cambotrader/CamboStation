import streamlit as st

def get_enabled_modules():
    st.sidebar.markdown("### ✅ Layout Module Selector")

    default_modules = [
        "🌐 TradingView Widget",
        "📈 Charts",
        "📊 Patterns",
        "🧠 Sentiment",
        "🧪 Strategy Lab",
        "✍️ Journal"
    ]

    return st.sidebar.multiselect("Active Modules", default_modules, default=default_modules)
