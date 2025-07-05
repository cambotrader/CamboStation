import streamlit as st
import json, os

from modules import module_dispatcher, manifest_viewer, module_toggle_control
from modules import voting_system, pattern_engine, sentiment_grid, execution_agent, strategy_planner
from modules import multiverse_simulator, reverse_planner, market_narrator, emotional_trade_filter, quantum_matrix

config_path = os.path.join(os.path.dirname(__file__), "config", "assets.config.json")

def load_config(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {
            "selected_asset": "stocks",
            "engine_map": {
                "stocks": "grok",
                "options": "tradegpt",
                "futures": "grok",
                "crypto": "gemini",
                "forex": "chatgpt",
                "bonds": "gemini"
            }
        }

config = load_config(config_path)
assets = list(config["engine_map"].keys())

# Sidebar
st.sidebar.title("🧭 CamboStation Control Panel")
selected_asset = st.sidebar.selectbox("Select Asset Class", assets, index=assets.index(config["selected_asset"]))
ai_engine = config["engine_map"].get(selected_asset, "unspecified")

# Save selection
config["selected_asset"] = selected_asset
with open(config_path, "w", encoding="utf-8") as f:
    json.dump(config, f, indent=2)

# Tabs
st.title("CamboStation Quantum OS™")
tab_main, tab_manifest, tab_placeholders, tab_toggle = st.tabs([
    "📊 Dashboard", 
    "🧩 Build Manifest", 
    "🧠 Module Placeholders",
    "🧩 Module Toggles"
])

with tab_main:
    st.subheader(f"📊 Active Asset Class: `{selected_asset.upper()}`")
    st.markdown(f"🧠 AI Routing Engine: `{ai_engine}`")
    st.info("Modules are activated based on asset-specific registry.")
    module_dispatcher.dispatch_modules(selected_asset)

with tab_manifest:
    manifest_viewer.render_manifest_status()

with tab_placeholders:
    st.markdown("### 📦 Feature Stack Modules")
    voting_system.render()
    pattern_engine.render()
    sentiment_grid.render()
    execution_agent.render()
    strategy_planner.render()

    st.markdown("### 🔮 Expansion Modules")
    multiverse_simulator.render()
    reverse_planner.render()
    market_narrator.render()
    emotional_trade_filter.render()
    quantum_matrix.render()

with tab_toggle:
    module_toggle_control.render_toggles()
