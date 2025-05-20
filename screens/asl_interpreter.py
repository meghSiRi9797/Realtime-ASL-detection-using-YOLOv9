import streamlit as st
from utils.detection import detect_image, detect_video, detect_webcam

def show(model_choice, detection_mode):
    st.title("ASL Interpreter")

    model_path = f"models/{model_choice}.pt"
    # st.info(f"Model loaded: {model_path}")

    if detection_mode == "Image":
        uploaded = st.file_uploader("📷 Upload an Image", type=["jpg", "jpeg", "png"])
        if uploaded:
            st.image(uploaded, caption="Uploaded Image", use_container_width=True)
            with st.spinner("Detecting..."):
                detect_image(uploaded, model_path)

    elif detection_mode == "Video":
        uploaded = st.file_uploader("🎥 Upload a Video", type=["mp4", "avi", "mov"])
        if uploaded:
            with st.spinner("Processing video..."):
                detect_video(uploaded, model_path)

    elif detection_mode == "Webcam":
        detect_webcam(model_path)
