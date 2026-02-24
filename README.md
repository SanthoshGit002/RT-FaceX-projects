# <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=35&pause=1000&color=7C6AF7&center=true&vCenter=true&width=600&lines=😴+Drowsiness+Recognition;🚗+Stay+Alert,+Stay+Safe!;👁️+Real-Time+Eye+Tracking" alt="Typing SVG" />

<div align="center">

![Driver Safety](https://img.shields.io/badge/Driver-Safety%20System-7c6af7?style=for-the-badge&logo=car&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-00d26a?style=for-the-badge&logo=statuspage&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-f76a8a?style=for-the-badge&logo=opensourceinitiative&logoColor=white)

<br/>

```
╔═══════════════════════════════════════════════════════════╗
║   👁️  EYES OPEN  →  ✅ Safe        EAR > 0.25            ║
║   😴  EYES CLOSED → ⚠️  ALERT!     EAR < 0.25 (20 frames) ║
╚═══════════════════════════════════════════════════════════╝
```

</div>

---

## 🌟 What is This?

> **A real-time AI-powered drowsiness detection system** that monitors your eyes through a webcam. If your eyes stay closed too long — **BOOM 🔊 — an alarm fires instantly!**

Perfect for **drivers, night workers, and students** who need to stay alert.

---

## ✨ Features

```
🎥  Real-time webcam monitoring
👁️  68-point facial landmark detection  
📐  Eye Aspect Ratio (EAR) algorithm
⚠️  Instant audio alert system
📊  Live drowsiness counter
▶️  One-click Start / Stop controls
🌐  Beautiful Streamlit web interface
```

---

## 🛠️ Tech Stack

<div align="center">

### 💻 Language
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

### 🎨 Framework & UI
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

### 👁️ Computer Vision
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![Dlib](https://img.shields.io/badge/Dlib-008000?style=for-the-badge&logo=buffer&logoColor=white)

### 🔢 Scientific Computing
![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?style=for-the-badge&logo=scipy&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)

</div>

---

## ⚙️ How It Works

```
📷 WEBCAM CAPTURES FRAME
         ↓
🔍 DLIB DETECTS FACE
         ↓
📍 68 FACIAL LANDMARKS EXTRACTED
         ↓
👁️ LEFT EYE + RIGHT EYE POINTS ISOLATED
         ↓
📐 EAR = (A + B) / (2 × C) CALCULATED
         ↓
    ┌────────────────────────────┐
    │  EAR < 0.25?               │
    │  YES → flag++              │
    │  NO  → flag = 0 (reset)    │
    └────────────────────────────┘
         ↓
    flag ≥ 20 frames?
    YES → 🚨 ALERT! playsound("3.wav")
```

---

## 🚀 Quick Start

### Step 1 — Clone
```bash
git clone https://github.com/SanthoshGit002/RT-FaceX-Project.git
cd RT-FaceX-Project
```

### Step 2 — Install Dependencies
```bash
pip install streamlit opencv-python dlib imutils scipy playsound
```

### Step 3 — Download Model
```
📥 Download: shape_predictor_68_face_landmarks.dat
📁 Place in: models/ folder
```
> 🔗 Download from: [dlib.net model files](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2)

### Step 4 — Run 🚀
```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
😴 RT-FaceX-Project/
│
├── 🐍 app.py                        ← Main application
├── 🔊 3.wav                         ← Alert sound
├── 📁 models/
│   └── 🧠 shape_predictor_68_face_landmarks.dat
└── 📄 README.md
```

---

## 📐 EAR Formula

```
        |p2-p6| + |p3-p5|
EAR =  ─────────────────────
            2 × |p1-p4|

p1, p4 = horizontal eye points
p2, p3, p5, p6 = vertical eye points

EAR ≈ 0.3  →  Eyes OPEN   ✅
EAR ≈ 0.0  →  Eyes CLOSED 😴
```

---

## 👨‍💻 Developer

<div align="center">

![Developer](https://img.shields.io/badge/Developer-Santhosh-7c6af7?style=for-the-badge&logo=github&logoColor=white)
![Role](https://img.shields.io/badge/Role-Full%20Stack%20Developer-f76a8a?style=for-the-badge&logo=code&logoColor=white)

**GitHub:** [@SanthoshGit002](https://github.com/SanthoshGit002)

</div>

---

<div align="center">

⭐ **Star this repo if you found it helpful!** ⭐

![Made with Love](https://img.shields.io/badge/Made%20with-❤️-f76a8a?style=for-the-badge)
![Python](https://img.shields.io/badge/Powered%20by-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

</div>
