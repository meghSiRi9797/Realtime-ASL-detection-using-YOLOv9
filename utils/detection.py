import streamlit as st
from PIL import Image
from collections import deque
import tempfile
from ultralytics import YOLO
import cv2
from gtts import gTTS
import playsound
import os

# Load model only once
@st.cache_resource
def load_model(model_path):
    return YOLO(model_path)

# Speak text using gTTS
from gtts import gTTS
import os
import time
import pygame

from gtts import gTTS
import os
from playsound import playsound

def speak_once(text):
    tts = gTTS(text=text, lang='en')
    filename = "temp_audio.mp3"
    tts.save(filename)
    playsound(filename)
    os.remove(filename)

# Stable prediction logic
def get_stable_prediction(predictions, threshold=3):
    if len(predictions) < threshold:
        return None
    last = predictions[-1]
    if all(p == last and p != '' for p in list(predictions)[-threshold:]):
        return last
    return None

# Detect in image
def detect_image(image_file, model_path):
    model = load_model(model_path)
    img = Image.open(image_file).convert("RGB")
    results = model.predict(img)
    annotated_img = results[0].plot()

    labels = [model.names[int(cls)] for cls in results[0].boxes.cls] if results[0].boxes else []

    if labels:
        unique_letters = " ".join(sorted(set(labels)))
        st.image(annotated_img, caption=f"Prediction: {unique_letters}", use_container_width=True)
        st.success(f"Detected: {unique_letters}")
        speak_once(unique_letters)
        return annotated_img, unique_letters
    else:
        st.image(annotated_img, caption="No signs detected", use_container_width=True)
        st.warning("No signs detected.")
        return annotated_img, ""

# Detect in uploaded video
def detect_video(video_file, model_path):
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(video_file.read())
    tfile.flush()
    cap = cv2.VideoCapture(tfile.name)

    if not cap.isOpened():
        st.error("Could not open video.")
        return

    model = load_model(model_path)
    stframe = st.empty()
    prediction_buffer = deque(maxlen=5)
    last_spoken = None
    frame_interval = 3
    frame_count = 0
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    progress = st.progress(0)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1
        if frame_count % frame_interval != 0:
            continue

        results = model.predict(frame)
        annotated = results[0].plot()
        stframe.image(annotated, channels="BGR", use_container_width=True)

        labels = [model.names[int(cls)] for cls in results[0].boxes.cls] if results[0].boxes else []
        prediction = " ".join(sorted(set(labels)))
        prediction_buffer.append(prediction)

        confirmed = get_stable_prediction(prediction_buffer, threshold=3)

        if confirmed and confirmed != last_spoken:
            st.success(f"Detected: {confirmed}")
            speak_once(confirmed)
            last_spoken = confirmed

        progress.progress(min(frame_count / total_frames, 1.0))

    cap.release()
    cv2.destroyAllWindows()
    progress.empty()

# Detect in webcam
def detect_webcam(model_path):
    cap = cv2.VideoCapture(0)
    model = load_model(model_path)
    stframe = st.empty()
    prediction_buffer = deque(maxlen=5)
    last_spoken = None
    frame_interval = 3
    frame_count = 0

    st.info("To quit, press the stop button in Streamlit (top right).")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            st.warning("Cannot access webcam.")
            break

        frame_count += 1
        if frame_count % frame_interval != 0:
            continue

        results = model.predict(frame)
        annotated = results[0].plot()
        stframe.image(annotated, channels="BGR", use_container_width=True)

        labels = [model.names[int(cls)] for cls in results[0].boxes.cls] if results[0].boxes else []
        prediction = " ".join(sorted(set(labels)))
        prediction_buffer.append(prediction)

        confirmed = get_stable_prediction(prediction_buffer, threshold=3)

        if confirmed and confirmed != last_spoken:
            st.success(f"Detected: {confirmed}")
            speak_once(confirmed)
            last_spoken = confirmed

    cap.release()
    cv2.destroyAllWindows()
