# Import necessary libraries

import cv2
import numpy as np
import mediapipe as mp

# Setup MediaPipe for hand detection

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.8)
mp_draw = mp.solutions.drawing_utils

# Start the webcam

cam = cv2.VideoCapture(0)
canvas = None

draw = False  # Toggle drawing mode
prev_x, prev_y = 0, 0

def count_fingers(hand_landmarks):
    fingers = []
    tip_ids = [4, 8, 12, 16, 20]

    for i in range(1, 5):  # Skip thumb
        if hand_landmarks.landmark[tip_ids[i]].y < hand_landmarks.landmark[tip_ids[i] - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)
    return sum(fingers)

while True:
    ret, frame = cam.read()
    if not ret:
        break

# Flip the frame horizontally (mirror view)

    frame = cv2.flip(frame, 1)

# Initialize canvas to match the frame size
    if canvas is None:
        canvas = np.zeros_like(frame)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
# Process the frame to find hands
    result = hands.process(rgb)
    # If hands are detected
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Draw hand landmarks on the frame
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            # Get the position of the index fingertip
            h, w, _ = frame.shape
            index_finger = hand_landmarks.landmark[8]
            cx, cy = int(index_finger.x * w), int(index_finger.y * h)
            # Count raised fingers
            fingers_up = count_fingers(hand_landmarks)

            if fingers_up == 1:
                draw = True
            elif fingers_up == 2:
                draw = False
            # If drawing mode is on, draw on the canvas
            if draw:
                if prev_x == 0 and prev_y == 0:
                    prev_x, prev_y = cx, cy
                else:
                    canvas = cv2.line(canvas, (prev_x, prev_y), (cx, cy), (0, 255, 0), 5)
                    prev_x, prev_y = cx, cy
            else:
                prev_x, prev_y = 0, 0  # Reset previous points

    combined = cv2.add(frame, canvas)
    cv2.putText(combined, "Drawing: " + str(draw), (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255) if not draw else (0, 255, 0), 2)

    cv2.imshow("Gesture Whiteboard", combined)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('c'):
        canvas = np.zeros_like(frame)

cam.release()
cv2.destroyAllWindows()
