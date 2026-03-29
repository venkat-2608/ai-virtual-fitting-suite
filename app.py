import streamlit as st
import cv2
import numpy as np

from measurement import extract_measurements
from size_predictor import recommend_size

st.set_page_config(page_title="AI Virtual Fitting Suite")

st.title("AI Virtual Fitting Suite")

uploaded = st.file_uploader(
    "Upload image",
    type=["jpg", "jpeg", "png"]
)

if uploaded:

    file_bytes = np.asarray(bytearray(uploaded.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    st.image(img, channels="BGR", use_container_width=True)

    measurements = extract_measurements(img)

    if measurements is None:

        st.error("Body landmarks not detected. Try a clearer full-body image.")

    else:

        shoulder = measurements["shoulder_cm"]
        waist = measurements["waist_cm"]

        size = recommend_size(shoulder, waist)

        st.subheader("Estimated Body Measurements")

        st.json(measurements)

        st.subheader("Recommended Size")

        st.success(size)