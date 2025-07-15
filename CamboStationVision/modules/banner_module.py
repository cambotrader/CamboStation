import streamlit as st

def render_banner():
    st.markdown("""
        <div style='text-align: center; padding: 10px 0;'>
            <h1 style='font-size: 28px; margin-bottom: 5px;'> CamboStation™ Vision</h1>
            <h3 style='font-weight: normal; color: #888;'>Trade with Vision • Learn with Purpose • Evolve with AI</h3>
            <hr style='margin-top: 10px; margin-bottom: 20px;'>
        </div>
    """, unsafe_allow_html=True)
