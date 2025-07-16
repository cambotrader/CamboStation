import streamlit as st
import json
import os

def render_manifest_status():
    st.subheader("🧩 Build Manifest Status")

    manifest_path = os.path.join(os.path.dirname(__file__), "..", "config", "modules.manifest.json")

    try:
        with open(manifest_path, "r", encoding="utf-8-sig") as f:
            manifest = json.load(f)
    except Exception as e:
        st.error(f"❌ Could not load manifest: {e}")
        return

    # Phase status
    for phase, modules in manifest.get("phases", {}).items():
        st.markdown(f"### {phase}")
        for module, status in modules.items():
            indicator = "✅" if status else "🟥"
            st.write(f"{indicator} `{module}`")

    # Feature stack
    st.markdown("### 📦 Feature Stack")
    for module, status in manifest.get("features", {}).items():
        indicator = "✅" if status else "🟥"
        st.write(f"{indicator} `{module}`")

    # Expansion modules
    st.markdown("### 🔮 Expansion Deck")
    for module, status in manifest.get("expansion", {}).items():
        indicator = "✅" if status else "🟥"
        st.write(f"{indicator} `{module}`")
