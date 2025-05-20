#  ASL Detection Platform using YOLOv9

> Detect American Sign Language (ASL) from images, videos, or real-time webcam using state-of-the-art YOLOv9 models.  
> This platform translates signs into text and speaks the output aloud using text-to-speech.

## 📸 Demo Preview

![ASL Demo](assets/demo.gif)  <!-- Add your demo video or GIF here -->

---
## 🌐 Live Demo
👉 [Click here to open the ASL Detection App](https://realtime-asl-detection-using-yolov9.streamlit.app)

A real-time American Sign Language (ASL) detection app built with **YOLOv9** and **Streamlit**...
---

##  Features

- 🎯 Real-time ASL detection from **image**, **video**, or **webcam**
- 🤖 Uses pretrained **YOLOv9** models (`yolov9c.pt`)
- 🔊 Built-in **text-to-speech** that speaks out detected signs
- 🧠 Modular and clean **Streamlit UI**
- 🌐 Deployed live via Streamlit Cloud

---

## About the Project

This project was developed to help bridge the communication gap for individuals who rely on sign language.  
It uses YOLOv9 (You Only Look Once, version 9) to detect hand signs and instantly convert them to spoken words.

## Installation

```bash
git clone https://github.com/yourusername/asl-detection.git
cd asl-detection
pip install -r requirements.txt
streamlit run app.py
