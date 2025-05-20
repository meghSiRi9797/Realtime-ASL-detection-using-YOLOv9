# detection.py

import streamlit as st
from PIL import Image
from collections import deque
import tempfile
import cv2
from ultralytics import YOLO
from gtts import gTTS
import tempfile
import os
import streamlit.components.v1 as components

@st.cache_resource
def load_model(model_path):
    try:
        return YOLO(model_path)
    except Exception as e:
        st.error(f"Model loading failed: {e}")
        raise

def speak_text(text):
    if not text:
        return
    # HTML + JS to speak the text automatically in browser
    js_code = f"""
    <script>
    var msg = new SpeechSynthesisUtterance("{text}");
    msg.rate = 0.9;
    msg.lang = 'en-US';
    window.speechSynthesis.cancel();  // stop any ongoing speech
    window.speechSynthesis.speak(msg);
    </script>
    """
    components.html(js_code, height=0, width=0)


#def speak_once(text):
    #if not text:
    #    return
  #  try:
        # Generate speech with gTTS
       # tts = gTTS(text=text, lang='en')
        
        # Create a temporary file
       # with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
          #  tts.save(tmp_file.name)
            # Play audio in Streamlit
         #   st.audio(tmp_file.name, format="audio/mp3")
        
        # Remove temp file immediately after playing
        #os.unlink(tmp_file.name)
        
   # except Exception as e:
   #     print(f"TTS error: {e}")


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
        speak_text(unique_letters)
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
            speak_text(confirmed)
            last_spoken = confirmed

        progress.progress(min(frame_count / total_frames, 1.0))

    cap.release()
    cv2.destroyAllWindows()
    progress.empty()

# Detect in webcam
def detect_webcam(model_path):
    # Initialize the “webcam_running” flag in session_state
    if 'webcam_running' not in st.session_state:
        st.session_state.webcam_running = False

    # Start / Stop buttons
    start = st.button("Start Webcam", use_container_width=True)
    stop  = st.button("Stop Webcam",  use_container_width=True)

    if start:
        st.session_state.webcam_running = True
    if stop:
        st.session_state.webcam_running = False

    # When the webcam is running, enter the loop
    if st.session_state.webcam_running:
        cap = cv2.VideoCapture(0)
        model = load_model(model_path)
        stframe = st.empty()
        prediction_buffer = deque(maxlen=5)
        last_spoken = None
        frame_interval = 3
        frame_count = 0

        # Only show this while streaming
        st.info("🔴 Webcam running… click ‘Stop Webcam’ to end.")

        while st.session_state.webcam_running:
            ret, frame = cap.read()
            if not ret:
                st.warning("Cannot access webcam.")
                break

            frame_count += 1
            if frame_count % frame_interval != 0:
                continue

            # Run inference
            results   = model.predict(frame)
            annotated = results[0].plot()
            stframe.image(annotated, channels="BGR", use_container_width=True)

            # Aggregate stable prediction
            labels     = [model.names[int(c)] for c in results[0].boxes.cls] if results[0].boxes else []
            prediction = " ".join(sorted(set(labels)))
            prediction_buffer.append(prediction)
            confirmed = get_stable_prediction(prediction_buffer, threshold=3)

            if confirmed and confirmed != last_spoken:
                st.success(f"Detected: {confirmed}")
                speak_text(confirmed)
                last_spoken = confirmed

        # Tear down
        cap.release()
        stframe.empty()
        st.success("🛑 Webcam stopped.")
