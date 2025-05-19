import streamlit as st
from streamlit_option_menu import option_menu
from screens import asl_interpreter, home, reference
import os

os.environ["STREAMLIT_WATCHER_TYPE"] = "none"

# Load CSS
with open("styles/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Top Navigation
selected = option_menu(
    menu_title=None,
    options=["Home", "ASL Interpreter", "Reference"],
    icons=["house", "camera", "book"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal"
)

# Page Routing
if selected == "Home":
    from screens import home
    home.show()

elif selected == "ASL Interpreter":
    from screens import asl_interpreter

    # Sidebar 
    st.sidebar.title("🛠️ Select Options")
    model_choice = st.sidebar.selectbox(
        "Select Model",
        ["yolov9c"],
        index=0
    )
    detection_mode = st.sidebar.radio(
        "Detection Mode",
        ["Image", "Video", "Webcam"],
        index=0
    )

    # Pass to interpreter
    asl_interpreter.show(model_choice, detection_mode)

elif selected == "Reference":
    from screens import reference
    reference.show()
