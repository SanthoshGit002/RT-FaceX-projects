import streamlit as st
import cv2
import dlib
import imutils
import time
from imutils import face_utils
from scipy.spatial import distance
from playsound import playsound



# Streamlit UI
st.markdown("<h1>🚗 DROWSINESS RECOGNITION</h1>", unsafe_allow_html=True)

frame_placeholder = st.empty()
count_placeholder = st.empty()
status_placeholder = st.empty()

if "running" not in st.session_state:
    st.session_state.running = False
if "alert_triggered" not in st.session_state:
    st.session_state.alert_triggered = False  # Track alert state

def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    return (A + B) / (2.0 * C)

# Load Dlib Models
detect = dlib.get_frontal_face_detector()
predict = dlib.shape_predictor("models/shape_predictor_68_face_landmarks.dat")

(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["right_eye"]

def start_detection():
    """Start the drowsiness detection."""
    st.session_state.running = True
    st.session_state.alert_triggered = False
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        status_placeholder.error("❌ Error: Camera not accessible.")
        return

    flag = 0
    thresh = 0.25  # EAR Threshold
    frame_check = 20  # Frames to trigger alert

    while st.session_state.running:
        ret, frame = cap.read()
        if not ret or frame is None:
            status_placeholder.error("❌ Error: Couldn't capture frame.")
            break
        
        frame = imutils.resize(frame, width=450)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        subjects = detect(gray, 0)

        for subject in subjects:
            shape = predict(gray, subject)
            shape = face_utils.shape_to_np(shape)
            
            leftEye = shape[lStart:lEnd]
            rightEye = shape[rStart:rEnd]
            leftEAR = eye_aspect_ratio(leftEye)
            rightEAR = eye_aspect_ratio(rightEye)
            ear = (leftEAR + rightEAR) / 2.0

            leftEyeHull = cv2.convexHull(leftEye)
            rightEyeHull = cv2.convexHull(rightEye)
            cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
            cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)

            if ear < thresh:
                flag += 1
            else:
                flag = 0
                st.session_state.alert_triggered = False  # Reset alert when eyes are open

            count_placeholder.markdown(f"<p class='info-text'>**Drowsiness Count: `{flag}`**</p>", unsafe_allow_html=True)

            if flag >= frame_check and not st.session_state.alert_triggered:
                status_placeholder.markdown("<p class='drowsy-alert'>⚠️ **Drowsiness Alert! Stay Awake!**</p>", unsafe_allow_html=True)
                playsound("3.wav") 
                st.session_state.alert_triggered = True  # Mark alert as sent
                time.sleep(3)  # Wait before allowing another alert
                status_placeholder.empty()  # Hide alert after 5 sec
				
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_placeholder.image(frame, channels="RGB")

    cap.release()
    status_placeholder.success("✅ Camera Stopped")
    frame_placeholder.empty()
    count_placeholder.empty()

def stop_detection():
    """Stop the drowsiness detection."""
    st.session_state.running = False

st.markdown('<div style="display: flex; justify-content: center; gap: 20px; margin-top: 20px;">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 1])
with col1:
    if st.button("▶️ Start"):
        start_detection()
with col2:
    if st.button("⏹ Stop"):
        stop_detection()
st.markdown('</div>', unsafe_allow_html=True)
