import streamlit as st
import traceback

st.write("App started ✅")

try:
    from utils.detection import load_model
    st.write("Imported load_model ✅")

    model = load_model("models/yolov9c.pt")
    st.success("Model loaded ✅")

except Exception as e:
    st.error("Crash detected ❌")
    st.text(traceback.format_exc())
