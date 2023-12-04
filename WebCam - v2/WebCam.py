import cv2
import numpy as np

webcam = cv2.VideoCapture(1)

min = np.array([0, 10, 0])
max = np.array([190, 190, 190])

if webcam.isOpened():
    print("Cam conect sucessuful!!")
    while True:
        validation, frames = webcam.read()
        hsv = cv2.cvtColor(frames, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, min, max)
        #print(frames.shape)
        
        cv2.line(frames, (0, 217), (120, 217), (255, 0, 0), 4)
        cv2.line(frames, (120, 217), (120, 360), (255, 0, 0), 4)
        cv2.line(frames, (640, 217), (520, 217), (255, 0, 0), 4)
        cv2.line(frames, (520, 217), (520, 360), (255, 0, 0), 4)
        
        cv2.imshow("Video WEBCAM - Index 1", frames)
        #cv2.imshow("Mask", mask)
        key = cv2.waitKey(1)
        if key == 27:
            break

cv2.release()
cv2.destroyAllWindows()
