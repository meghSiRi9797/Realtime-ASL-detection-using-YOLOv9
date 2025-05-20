# screens/home.py

import streamlit as st

def show():
    # Create a two-column layout: one for logo, one for title
    col1, col2 = st.columns([2, 5])
    
    with col1:
        st.image("download.jpg", width=200)  # Adjust path and size
   
    with col2:
        st.markdown("<h1 style='font-size: 40x; margin-top: 5px;'> ASL Detection Platform</h1>", unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""

    **American Sign Language (ASL)** is a natural language used by the Deaf and hard-of-hearing community in the United States and parts of Canada. ASL is visual and uses hand gestures, facial expressions, and body posture to convey meaning.

    Despite being a rich and expressive language, real-time understanding of ASL through computers remains a challenge — especially for accessibility in public spaces, education, and healthcare.

    ##  Project Overview

    This project aims to build an intelligent, real-time ASL interpreter using **YOLOv9**, one of the most advanced object detection models available today.

    Using this platform, you can:

    - Upload **images** containing ASL signs
    - Upload **videos** with continuous sign gestures
    - Use your **webcam** for real-time sign detection

    Once a sign is detected, the system uses **Text-to-Speech (TTS)** to speak the interpreted word or letter aloud.

    ##  Model Used – YOLOv9

    - **YOLOv9 (You Only Look Once)** is a state-of-the-art, real-time object detection model.
    - It's optimized for both **speed** and **accuracy**, making it ideal for detecting fast hand gestures.
    - Our system currently supports models like:
        - `yolov9c`: Compact and fast
       

    ##  Real-World Use Case

    This platform can be extended and deployed in:

    - **Classrooms** to help teachers understand Deaf students
    - **Hospitals** for basic patient communication
    - **Kiosks** or **customer service** counters for public accessibility
    - **Mobile apps** to assist in everyday interactions

    This is a step forward in creating inclusive technology that bridges the communication gap between the hearing and Deaf communities.

    ---
    
     **Try it out now** by going to the **ASL Interpreter** tab above!
    """)
