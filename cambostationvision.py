from modules.banner_module import render_banner
from modules.strategy_lab import render_strategy_lab
import streamlit as st

# ─────────────────────────────────────────────
# Import Modules (adjust based on what you've deployed)
# ─────────────────────────────────────────────
from modules.layout_controller import get_enabled_modules
from modules.tradingview_widget import render_tradingview_widget
from modules.chart_tab import render_chart_tab  # Only include if chart_tab.py exists
from modules.pattern_recognizer import render_pattern_tab
from modules.chart_pattern_detector import render_chart_pattern_tab
from modules.strategy_linker import link_detected_patterns_to_strategy
from modules.pattern_logbook import render_logbook_viewer  # Optional: if logbook is deployed

# ─────────────────────────────────────────────
# App Title + Header
# ─────────────────────────────────────────────
st.set_page_config(page_title="CamboStation™", layout="wide")
render_banner()
st.title("🎯 CamboStation™ Cockpit Interface")

st.markdown("#### Tactical Trading Dashboard — Modular Pattern & Strategy Intelligence")
st.markdown("---")

# ─────────────────────────────────────────────
selected_tab = st.selectbox("🧭 Navigate CamboStation Modules", [
    "📊 Charts",
    "📐 Structure Scanner",
    "📈 Candle Scanner",
    "🧠 Strategy Lab",
    "✍️ Pattern Journal",
    "🌐 Live Widget"
])
if selected_tab == "📊 Charts":
    render_chart_tab()

elif selected_tab == "📐 Structure Scanner":
    render_chart_pattern_tab()

elif selected_tab == "📈 Candle Scanner":
    render_pattern_tab()

elif selected_tab == "🧠 Strategy Lab":
    render_strategy_lab()

elif selected_tab == "✍️ Pattern Journal":
    render_logbook_viewer()

elif selected_tab == "🌐 Live Widget":
    render_tradingview_widget()




# 🔮 Future Modules
# if "🧪 Strategy Lab" in enabled_modules:
#     render_strategy_lab()  ← You can add this after deploying strategy lab tab

# if "🧠 Sentiment" in enabled_modules:
#     render_sentiment_tab()
