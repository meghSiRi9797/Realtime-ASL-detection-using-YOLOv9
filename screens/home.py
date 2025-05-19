import streamlit as st

def show():
    st.title("🧬 Welcome to the ASL Detection Platform")
    st.markdown("""
    This platform allows you to detect American Sign Language (ASL) gestures using pretrained YOLOv9 models.
    
    **Features:**
    - Choose between YOLOv9C and YOLOv9E models.
    - Detect ASL from images, videos, and webcam.
    - Text-to-Speech output for the predicted sign.
    
    Use the navigation bar above to explore!
    """)
