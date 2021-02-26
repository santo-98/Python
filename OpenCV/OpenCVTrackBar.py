import cv2
import numpy as np

def ok(x):
    pass

img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow('IMG1')

cv2.createTrackbar('B','IMG1', 0, 255, ok)
cv2.createTrackbar('G','IMG1', 0, 255, ok)
cv2.createTrackbar('R','IMG1', 0, 255, ok)
while(1):
    cv2.imshow('IMG1', img)
    if cv2.waitKey(1) == ord('s'):
        break
    b = cv2.getTrackbarPos('B', 'IMG1')
    g = cv2.getTrackbarPos('G', 'IMG1')
    r = cv2.getTrackbarPos('R', 'IMG1')
    img[:] = [b, g, r]
cv2.destroyAllWindows()
