# AI Virtual Fitting Suite

A simple AI-based application that estimates body measurements from a single image and recommends a clothing size. The system uses computer vision to detect body landmarks and calculate approximate measurements.

The project is built using **Streamlit, OpenCV, and MediaPipe Pose detection**.

---

## Features

* Upload a full-body image
* Detect body landmarks using MediaPipe
* Estimate shoulder and waist measurements
* Recommend a clothing size based on extracted measurements
* Simple interactive web interface using Streamlit

---

## Project Structure

```
VIRTUALTRYON
│
├── app.py               # Streamlit application
├── measurement.py       # Extract body measurements from image
├── size_predictor.py    # Size recommendation logic
├── requirements.txt     # Project dependencies
```

---

## How It Works

### 1. Image Upload

The user uploads an image through the Streamlit interface.

### 2. Pose Detection

MediaPipe Pose identifies body landmarks such as:

* Shoulders
* Hips
* Head
* Ankles

### 3. Measurement Estimation

Using the detected landmarks, the system calculates:

* Shoulder width
* Waist width

A scaling factor is estimated using assumed average human height.

### 4. Size Recommendation

Example size logic:

```
XS  -> shoulder < 38 cm
S   -> 38 - 42 cm
M   -> 42 - 46 cm
L   -> 46 - 47 cm
XL  -> > 47 cm
```

---

## Installation

Clone the repository:

```
git clone https://github.com/yourusername/virtualtryon.git
cd virtualtryon
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Running the Application

Start the Streamlit app:

```
streamlit run app.py
```

The application will open in your browser.

---

## Dependencies

The project uses the following libraries:

* Streamlit
* OpenCV
* MediaPipe
* NumPy

All dependencies are listed in `requirements.txt`.

---

## Current Limitations

* Measurement accuracy depends on image quality
* Best results require a clear full-body image
* Uses an assumed average height for scaling
* Only basic size prediction is implemented

---

## Future Improvements

* More accurate body measurement estimation
* Support for multiple clothing categories
* Integration with virtual try-on visualization
* Machine learning based size recommendation
* Improved scaling using reference objects
