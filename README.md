# Virtual-Board

# 🖐️ Gesture-Based Virtual Whiteboard with MediaPipe & OpenCV

This project is a **virtual whiteboard** controlled entirely by **hand gestures** using a webcam. With the help of **MediaPipe** for real-time hand tracking and **OpenCV** for drawing, you can draw on the screen by simply raising a finger!

---

## 📌 Features

- Real-time hand detection using MediaPipe
- Draw on a virtual canvas using the index finger
- Use gesture-based commands:
  - ✋ 1 Finger Up → Start Drawing
  - ✋ 2 Fingers Up → Stop Drawing
- Press `'c'` to clear the canvas
- Press `'q'` to quit the application

---

## 🧰 Technologies Used

- **Python**
- **OpenCV**
- **MediaPipe**
- **NumPy**

---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/gesture-whiteboard.git
cd gesture-whiteboard

Controls
Gesture / Key	Action
✋ 1 Finger	Start Drawing
✋ 2 Fingers	Stop Drawing
c key	Clear the canvas
q key	Quit the application

🧠 How It Works
Uses MediaPipe Hands to detect hand landmarks in real time.

Tracks the index fingertip position to draw lines on a transparent canvas.

A count_fingers function determines how many fingers are raised.

Drawing is toggled based on finger count (1 = draw, 2 = stop).
