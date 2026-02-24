# 😴 Drowsiness Recognition System

A real-time driver drowsiness detection system that monitors eye activity using facial landmarks and triggers an alert when drowsiness is detected.

---

## 🎯 Overview

This system uses a webcam to continuously monitor the driver's eyes. It calculates the **Eye Aspect Ratio (EAR)** to detect if the eyes are closing for too long — and immediately plays an audio alert to wake the driver up.

---

## ✨ Features

- 🎥 Real-time webcam face detection
- 👁️ Eye Aspect Ratio (EAR) calculation
- ⚠️ Instant drowsiness alert with sound
- 📊 Live drowsiness counter display
- ▶️ Start / ⏹ Stop controls
- 🌐 Beautiful Streamlit web UI

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| Streamlit | Web UI framework |
| OpenCV | Video capture & processing |
| Dlib | Face & landmark detection |
| SciPy | EAR distance calculation |
| imutils | Frame resizing utilities |
| playsound | Audio alert playback |

---

## ⚙️ How It Works

1. Webcam captures live video frames
2. Dlib detects face and 68 facial landmarks
3. Eye landmarks are extracted (left & right)
4. EAR is calculated for both eyes
5. If EAR < 0.25 for 20+ frames → **ALERT triggered!**
6. Audio alarm plays to wake the driver

---

## 🚀 How to Run

### 1. Clone the repository
```
git clone https://github.com/SanthoshGit002/RT-FaceX-Project.git
cd RT-FaceX-Project
```

### 2. Install dependencies
```
pip install streamlit opencv-python dlib imutils scipy playsound
```

### 3. Download the model
- Download `shape_predictor_68_face_landmarks.dat`
- Place it inside a `models/` folder

### 4. Run the app
```
streamlit run app.py
```

---

## 📁 Project Structure
```
RT-FaceX-Project/
│
├── app.py                  # Main application
├── 3.wav                   # Alert sound file
├── models/
│   └── shape_predictor_68_face_landmarks.dat
└── README.md
```

---

## 👨‍💻 Developer

**Santhosh** — Full Stack Developer
GitHub: [@SanthoshGit002](https://github.com/SanthoshGit002)

---

## 📄 License
MIT License
