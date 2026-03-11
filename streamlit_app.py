import streamlit as st
import cv2
import numpy as np
import av
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase
import os
import gdown
import pandas as pd
import time

if "mask_count" not in st.session_state:
    st.session_state.mask_count = 0

if "no_mask_count" not in st.session_state:
    st.session_state.no_mask_count = 0

MODEL_PATH = "face_mask_detector.h5"

def download_model():

    if not os.path.exists(MODEL_PATH):

        file_id = "1LmR-juV4KXUmJvuDu5hxB8K0oDdMJukF"

        url = f"https://drive.google.com/uc?id={file_id}"

        print("Downloading model from Google Drive...")

        gdown.download(url, MODEL_PATH, quiet=False)

# Build model architecture
def build_model():

    model = Sequential([
        Conv2D(32, (3,3), activation='relu', input_shape=(150,150,3)),
        MaxPooling2D(2,2),

        Conv2D(64, (3,3), activation='relu'),
        MaxPooling2D(2,2),

        Flatten(),
        Dense(128, activation='relu'),
        Dropout(0.3),
        Dense(1, activation='sigmoid')
    ])

    return model


# Load model + cascade
@st.cache_resource
def load_resources():

    download_model()

    model = build_model()

    model.load_weights(MODEL_PATH)

    face_cascade = cv2.CascadeClassifier(
        "haarcascade_frontalface_default.xml"
    )

    print("Cascade loaded:", not face_cascade.empty())

    return model, face_cascade


model, face_cascade = load_resources()

frame_skip = 3

class VideoProcessor(VideoProcessorBase):

    def __init__(self):
        self.mask_count = 0
        self.no_mask_count = 0
        self.counter = 0

    def recv(self, frame):

        img = frame.to_ndarray(format="bgr24")

        self.counter += 1

        # Run detection every N frames
        if self.counter % frame_skip == 0:

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            faces = face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=4,
                minSize=(30,30)
            )

            for (x, y, w, h) in faces:

                face = img[y:y+h, x:x+w]

                # Frame resizing
                face = cv2.resize(face,(150,150))
                face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
                face = face.astype("float32")/255.0
                face = np.expand_dims(face, axis=0)

                pred = model(face, training=False).numpy()[0][0]

                if pred < 0.5:
                    label = "Mask"
                    color = (0,255,0)
                    self.mask_count += 1
                else:
                    label = "No Mask"
                    color = (0,0,255)
                    self.no_mask_count += 1

                cv2.rectangle(img,(x,y),(x+w,y+h),color,2)

                cv2.putText(
                    img,
                    label,
                    (x,y-10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    color,
                    2
                )

        return av.VideoFrame.from_ndarray(img, format="bgr24")


# Streamlit UI

st.title("Face Mask Detection ")

st.write("Real-time face mask detection using CNN and webcam.")

st.subheader("Detection Analytics")

col1, col2 = st.columns(2)

col1.metric("Mask Detected", st.session_state.mask_count)
col2.metric("No Mask Detected", st.session_state.no_mask_count)

chart_data = pd.DataFrame({
    "Category": ["Mask", "No Mask"],
    "Count": [
        st.session_state.mask_count,
        st.session_state.no_mask_count
    ]
})

st.bar_chart(chart_data.set_index("Category"))

st.subheader("Live Detection")

ctx = webrtc_streamer(
    key="mask-detection",
    video_processor_factory=VideoProcessor,

    media_stream_constraints={
        "video": True,
        "audio": False
    }
)

if ctx.video_processor:

    st.session_state.mask_count = ctx.video_processor.mask_count
    st.session_state.no_mask_count = ctx.video_processor.no_mask_count