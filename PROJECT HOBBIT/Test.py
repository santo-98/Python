import cv2 as cv
import numpy as np

messi = cv.imread("messi5.jpg")
logo = cv.imread("opencv-logo-white.png") 

row, col, channels = logo.shape
roi = messi[0:row,0:col]

gray = cv.cvtColor(logo,cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(gray,10,255,cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask) 

img1 = cv.bitwise_and(roi,roi, mask=mask_inv)

img2 = cv.bitwise_and(logo,logo, mask=mask)

blend =  cv.addWeighted(img1,0.7,img2,0.8,0)
messi[0:row,0:col] = blend
# test = np.zeros((512,512,3),dtype = "uint8")

cv.imshow("test", img1)
cv.imshow("test1", img2)
cv.imshow("test2",messi)

cv.waitKey(0)
cv.destroyAllWindows()