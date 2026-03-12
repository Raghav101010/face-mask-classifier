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

Same project is deployed to two separate clouds at separate commit.

    Railway -> added frame skipping and STUN server configuration: b60a4cbcda2df20f6a5d8939e8fed12623b54093

    HF Spaces -> Dockerized face mask detection app for railway deployment: 1d3e936a894fc62f95002c2a2e537679433e5ba4


Application Features

    Real-time face detection using Haar Cascade
    CNN-based mask classification
    Live webcam inference
    Real-time analytics dashboard
    Automatic model download from Google Drive for Hugging Face only
    Interactive Streamlit UI with dashboard
    Docker containerization for deployment

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
    CNN
    OpenCV
    Haar Cascade Face Detection
    Streamlit
    streamlit-webrtc
    NumPy
    Pandas
    Docker
    Railway
    Hugging Face Spaces
    

Real-Time Analytics

    The dashboard displays:
    Total masks detected
    Total no-mask detections
    Live bar chart visualization
    This provides real-time monitoring of mask compliance.

Project Structure

    face-mask-classifier

        streamlit_app.py
        Dockerfile
        requirements.txt
        haarcascade_frontalface_default.xml
        README.md
        .dockerignore
        .gitignore

The trained model is downloaded automatically at runtime.

Live Deployment 

    Hugging Face Space:
    https://huggingface.co/spaces/raghav101010/face-mask-classifier

    Railway Deployment:
    https://face-mask-app-production.up.railway.app
    Hosted using Docker container deployment on Railway

    Note: Due to browser WebRTC restrictions in some cloud environments, webcam streaming may close automatically on these platforms. The application works fully when run locally.

How to Run the Project Locally

    1. Clone Repository
        git clone https://github.com/raghav101010/face-mask-classifier.git
        cd face-mask-classifier
    2. Create Virtual Environment
        python -m venv .venv
    3. Activate environment
        Windows:
            .venv\Scripts\activate
        Mac/Linux:
            source .venv/bin/activate
    4. Install Dependencies
        pip install -r requirements.txt
    5. Run Streamlit App      
        streamlit run streamlit_app.py
        Open browser:
            http://localhost:8501

    Running with Docker
    1. Build the image:
        docker build -t face-mask-app .
    2. Run the container
        docker run -p 8501:8501 face-mask-app
    3. Open in browser:
        http://localhost:8501
        

Future Improvements

    Replace Haar Cascade with a deep learning face detector
    Improve model accuracy with larger datasets or transfer learning
    Face tracking
    Improve cloud deployment for stable webcam streaming
    Add REST API inference endpoint  

Author

    Raghwendra Mahato
    AI / Computer Vision Enthusiast