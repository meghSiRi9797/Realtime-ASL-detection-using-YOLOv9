import streamlit as st

def show():
    st.title("📖 Reference")
    st.markdown("""
    **Model Info**  
    - `yolov9c25best.pt`: Compact and optimized for speed.  
    - `yolov9e_best.pt`: Extended version with higher accuracy.

    **Supported Inputs**  
    - Images: PNG, JPG, JPEG  
    - Videos: MP4, AVI, MOV  
    - Webcam: Real-time detection

    **Libraries Used**
    - YOLOv9
    - OpenCV
    - Streamlit
    - pyttsx3 for speech
    """)