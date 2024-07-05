import cv2
import pygame
from sent_email import execute




cap = cv2.VideoCapture(0)

ret, frame = cap.read()


img_name = "opencv_frame.png"
cv2.imwrite(img_name, frame)
print("Screenshot take")
execute()

cap.release()

