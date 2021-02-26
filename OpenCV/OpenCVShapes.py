import cv2 as cv
img = cv.imread("opencv-master\samples\data\lena.jpg",1)

img = cv.line(img, (0,0), (255,255), (0,0,255), 3)
cv.imshow('SHOW',img)
cv.waitKey(0)