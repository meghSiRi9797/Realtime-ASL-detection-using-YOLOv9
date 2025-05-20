# screens/reference.py

import streamlit as st

def show():
    st.title(" Reference")

    st.markdown("""
    ##  Research Paper
    - **"Real Time American Sign Language Detection Using Yolo-v9"**  
      [View on arXiv](https://arxiv.org/pdf/2407.17950)

    ##  Libraries & Tools Used

    - [Ultralytics YOLOv9](https://github.com/ultralytics/ultralytics)  
      Official YOLOv9 GitHub implementation by Ultralytics.
    
    - [OpenCV](https://opencv.org/)  
      For image and video processing.
    
    - [Streamlit](https://streamlit.io/)  
      Web app framework used for UI and interaction.
    
    - [pyttsx3](https://pypi.org/project/pyttsx3/)  
      Python Text-to-Speech library used for speech output.

    ##  Dataset & Models
    - YOLOv9C pretrained weights are used for gesture detection.  
      These models are selected based on trade-offs between **speed** and **accuracy**.
    - Dataset is assumed to be a curated ASL dataset with labeled hand gestures (custom or open-source).

    ##  Supported Inputs
    - **Images**: `.png`, `.jpg`, `.jpeg`
    - **Videos**: `.mp4`, `.avi`, `.mov`
    - **Webcam**: Live detection through connected camera

    ---
    """)
