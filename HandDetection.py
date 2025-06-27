import cv2
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7)

# Mapping finger names for clarity
finger_joint_labels = {
    0: "Wrist",
    1: "Thumb-Meta", 2: "Thumb-Prox", 3: "Thumb-Dist", 4: "Thumb-Tip",
    5: "Index-Meta", 6: "Index-Prox", 7: "Index-Inter", 8: "Index-Tip",
    9: "Middle-Meta",10: "Middle-Prox",11: "Middle-Inter",12: "Middle-Tip",
    13:"Ring-Meta", 14:"Ring-Prox", 15:"Ring-Inter", 16:"Ring-Tip",
    17:"Pinky-Meta",18:"Pinky-Prox",19:"Pinky-Inter",20:"Pinky-Tip"
}

# Open webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # Flip for mirror view and convert color
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            for i, lm in enumerate(hand_landmarks.landmark):
                h, w, _ = frame.shape
                x, y = int(lm.x * w), int(lm.y * h)

                label = finger_joint_labels.get(i, str(i))
                cv2.putText(frame, label, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)

            # Optional: draw the hand connections
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Finger Joints", frame)
    if cv2.waitKey(1) & 0xFF == 27:  # ESC to quit
        break

cap.release()
cv2.destroyAllWindows()
