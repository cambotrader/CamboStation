from narrator_engine import narrate_session

def render_narrator_tab():
    import streamlit as st
    st.title("🎙️ Session Narrator")
    for story in narrate_session():
        st.markdown(story)
