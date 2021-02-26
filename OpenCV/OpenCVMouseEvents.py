import cv2
import numpy as np 

def click_event(a, x, y, flag, param):
    if a == cv2.EVENT_LBUTTONDOWN:
        print(x, " - ", y)
        cv2.imshow('image', img)

img = cv2.imread("opencv-master\samples\data\lena.jpg",1)
cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()