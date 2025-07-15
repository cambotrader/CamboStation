import streamlit as st
import json
import os

def load_manifest():
    manifest_path = os.path.join(os.path.dirname(__file__), "..", "config", "modules.manifest.json")
    try:
        with open(manifest_path, "r", encoding="utf-8-sig") as f:
            return manifest_path, json.load(f)
    except:
        return manifest_path, {}

def update_manifest(manifest_path, manifest):
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)

def render_toggles():
    st.subheader("🧩 Module Toggle Control Panel")

    manifest_path, manifest = load_manifest()

    if not manifest:
        st.error("Manifest could not be loaded.")
        return

    changed = False

    # Feature Toggles
    st.markdown("### 📦 Feature Stack")
    for key, value in manifest.get("features", {}).items():
        new_val = st.checkbox(f"{key}", value)
        if new_val != value:
            manifest["features"][key] = new_val
            changed = True

    # Expansion Toggles
    st.markdown("### 🔮 Expansion Deck")
    for key, value in manifest.get("expansion", {}).items():
        new_val = st.checkbox(f"{key}", value)
        if new_val != value:
            manifest["expansion"][key] = new_val
            changed = True

    if changed:
        update_manifest(manifest_path, manifest)
        st.success("✅ Manifest updated!")
