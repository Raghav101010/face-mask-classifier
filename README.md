---
title: Real-Time Face Mask Detection
emoji: 😷
colorFrom: blue
colorTo: green
sdk: docker
app_file: streamlit_app.py
pinned: false
---
Real-Time Face Mask Detection

A real-time computer vision application that detects whether a person is wearing a face mask using a Convolutional Neural Network (CNN) and live webcam input.

The application performs face detection, mask classification, and real-time analytics visualization through an interactive Streamlit dashboard.

Application Features

    Real-time face detection using Haar Cascade
    CNN-based mask classification
    Live webcam inference
    Real-time analytics dashboard
    Automatic model download from Google Drive
    Interactive Streamlit UI

Model Architecture

The model is a Convolutional Neural Network built using TensorFlow.

Architecture:

    Conv2D(32) → ReLU
    MaxPooling2D
    Conv2D(64) → ReLU
    MaxPooling2D
    Flatten
    Dense(128) → ReLU
    Dropout(0.3)
    Dense(1) → Sigmoid

Binary classification:
    -Mask
    -No Mask

Tech Stack

    Python
    TensorFlow
    OpenCV
    Streamlit
    streamlit-webrtc
    NumPy
    Pandas

Real-Time Analytics

    The dashboard displays:
    Total masks detected
    Total no-mask detections
    Live bar chart visualization
    This provides real-time monitoring of mask compliance.

Project Structure

    face-mask-classifier

        streamlit_app.py
        requirements.txt
        haarcascade_frontalface_default.xml
        README.md

The trained model is downloaded automatically at runtime.

Deployment at Hugging Face Space:

    https://huggingface.co/spaces/raghav101010/face-mask-classifier


Future Improvements

    Replace Haar Cascade with a deep learning face detector
    Improve model accuracy with larger datasets
    Deploy optimized lightweight model
    Add mask compliance analytics dashboard  

Author

    Raghwendra Mahato
    AI / Computer Vision Enthusiast