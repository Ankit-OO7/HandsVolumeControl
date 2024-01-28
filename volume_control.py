import cv2
import mediapipe as mp   # mediapipe provides tools for Hand Tracking
import pyautogui
x1 = y1 = x2 = y2 = 0    # it is used to store particular points of hand
webcam = cv2.VideoCapture(0)    # it starts the webcam, default webcam is indicated by 0
my_hands = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
while True:
    _, image = webcam.read()
    image = cv2.flip(image, 1)
    frame_height, frame_width, _ = image.shape
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    output = my_hands.process(rgb_image)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(image, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)
                if id == 8:
                    cv2.circle(img=image, center=(x, y), radius=10, color=(255, 0, 255), thickness=3)
                    x1 = x
                    y1 = y
                if id == 4:
                    cv2.circle(img=image, center=(x, y), radius=10, color=(255, 0, 255), thickness=3)
                    x2 = x
                    y2 = y
        dist = ((x2-x1)**2 + (y2-y1)**2)**(0.5)//4
        cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 5)   # It shows line between the forefinger and thumb
        if dist > 50:
            pyautogui.press("VolumeUp")
        else:
            pyautogui.press("VolumeDown")

    cv2.imshow("Hand Volume Control using Python", image)
    key = cv2.waitKey(10)
    if key == 27:  # When Esc is pressed window will close
        break

webcam.release()
cv2.destroyAllWindows()
