# ------------------------------------------------------
# AIRIS – AI Vision Assistant for the Visually Impaired
# Developed using YOLOv8 + OpenCV + Text-to-Speech
# ------------------------------------------------------

import cv2
import pyttsx3
from ultralytics import YOLO
import time

# ---------------------------
# Initialize Text-to-Speech
# ---------------------------
engine = pyttsx3.init()
engine.setProperty('rate', 160)    # Speech speed
engine.setProperty('volume', 1.0)  # Volume level (0.0 to 1.0)

# ---------------------------
# Load YOLOv8 Model
# ---------------------------
# yolov8n.pt = "nano" version (fast & lightweight)
# It will download automatically if not found
print("Loading YOLOv8 model...")
model = YOLO('yolov8n.pt')
print("Model loaded successfully.")

# ---------------------------
# Open Webcam
# ---------------------------
cap = cv2.VideoCapture(0)  # 0 = Default webcam
if not cap.isOpened():
    print("❌ Error: Could not open webcam.")
    exit()

print("\n✅ Airis system is now running...")
print("🔹 Press 'q' to quit.\n")

# ---------------------------
# Variables for timing speech
# ---------------------------
last_spoken = ""
last_time = 0

# ---------------------------
# Main Loop
# ---------------------------
while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Error: Failed to read from webcam.")
        break

    # Run YOLOv8 inference
    results = model(frame, stream=True)

    detected_objects = set()

    # Process detected boxes
    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls)
            label = model.names[cls_id]
            detected_objects.add(label)

            # Draw box and label
            coords = box.xyxy[0]
            x1, y1, x2, y2 = map(int, coords)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, label, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # Speak detected objects every few seconds
    if detected_objects:
        current_time = time.time()
        if current_time - last_time > 3:  # Speak every 3 seconds
            spoken_text = ", ".join(detected_objects)
            if spoken_text != last_spoken:
                print(f"👁 Detected: {spoken_text}")
                engine.say(f"I see {spoken_text}")
                engine.runAndWait()
                last_spoken = spoken_text
                last_time = current_time

    # Display video
    cv2.imshow("Airis - Real-Time Object Detection", frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ---------------------------
# Cleanup
# ---------------------------
cap.release()
cv2.destroyAllWindows()
engine.stop()
print("\n🔸 Airis system stopped.")